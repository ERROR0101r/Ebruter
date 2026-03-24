#!/usr/bin/env python3

import os
import sys
import time
import requests
import threading
import queue
import json
from urllib.parse import urljoin, urlparse
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

def install_package(package):
    try:
        __import__(package)
        return True
    except ImportError:
        print(f"📦 Installing {package}...")
        os.system(f"pip install {package}")
        return True

install_package("requests")
install_package("colorama")
import requests
from colorama import Fore, Style

class EbruterScanner:
    def __init__(self, target_url, threads=50, timeout=5):
        self.target_url = target_url.rstrip('/')
        self.threads = threads
        self.timeout = timeout
        self.found_items = []
        self.queue = queue.Queue()
        self.lock = threading.Lock()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        })
        self.start_time = None
        self.found_count = 0
        self.GREEN = Fore.GREEN
        self.RED = Fore.RED
        self.YELLOW = Fore.YELLOW
        self.CYAN = Fore.CYAN
        self.RESET = Style.RESET_ALL

    def load_default_wordlist(self):
        wordlist = [
            'admin', 'administrator', 'adminpanel', 'admincp', 'admin_area', 'adm', 'admins',
            'admin_login', 'admin_panel', 'admin.php', 'admin.asp', 'admin.aspx', 'admin.jsp',
            'wp-admin', 'wp-login', 'wp-admin.php', 'wp-login.php', 'dashboard', 'cpanel',
            'plesk', 'webmail', 'phpmyadmin', 'mysql', 'myadmin', 'pma', 'adminer',
            'backup', 'backups', 'old', 'new', 'test', 'dev', 'staging', 'beta', 'demo',
            'temp', 'tmp', 'cache', 'logs', 'log', 'error_log', 'debug', 'private',
            'secret', 'hidden', 'secure', 'protected', 'restricted', 'confidential',
            '.env', '.git', '.svn', '.hg', '.bzr', '.gitignore', '.htaccess', '.htpasswd',
            'config', 'configuration', 'settings', 'setup', 'install', 'configuration.php',
            'wp-config.php', 'wp-config.php.bak', 'config.php', 'config.php.bak', 'database.php',
            'db.php', 'db_config.php', 'settings.php', 'local.xml', 'app.config', 'web.config',
            'database', 'db', 'sql', 'dump', 'export', 'import', 'backup.sql', 'backup.zip',
            'backup.tar.gz', 'dump.sql', 'db_dump.sql', 'database.sql', 'data.sql',
            'api', 'v1', 'v2', 'v3', 'rest', 'graphql', 'api/v1', 'api/v2', 'api/v3',
            'api.php', 'api.asp', 'api.json', 'api.xml', 'swagger', 'swagger-ui',
            'robots.txt', 'sitemap.xml', 'sitemap.xml.gz', 'crossdomain.xml', 'humans.txt',
            'favicon.ico', 'index.php', 'index.html', 'index.asp', 'index.aspx', 'default.php',
            'default.html', 'home.php', 'home.html', 'main.php', 'main.html', 'login.php',
            'login.html', 'register.php', 'signup.php', 'signup.html', 'logout.php', 'logout',
            'backup.zip', 'backup.tar', 'backup.tar.gz', 'backup.rar', 'backup.7z',
            'old.zip', 'old.tar', 'old.tar.gz', 'copy.zip', 'copy.tar', 'copy.tar.gz',
            'index.php.bak', 'index.php~', 'index.php.swp', 'index.php.swo', 'config.php.bak',
            'config.php~', 'config.php.swp', 'wp-config.php.bak', 'wp-config.php~',
            '.git/config', '.git/HEAD', '.git/index', '.git/logs', '.git/refs',
            '.svn/entries', '.svn/wc.db', '.svn/format', '.svn/pristine',
            'composer.json', 'composer.lock', 'package.json', 'package-lock.json',
            'requirements.txt', 'Gemfile', 'Gemfile.lock', 'Cargo.toml', 'go.mod',
            'Makefile', 'Dockerfile', 'docker-compose.yml', 'Jenkinsfile', '.travis.yml',
            'phpinfo.php', 'info.php', 'test.php', 'test.html', 'test.asp', 'test.jsp',
            'phpmyadmin', 'mysql', 'myadmin', 'phpPgAdmin', 'pgadmin', 'adminer.php',
            'server-status', 'server-info', 'status', 'info', 'health', 'healthcheck',
            'upload', 'uploads', 'files', 'media', 'images', 'img', 'assets', 'static',
            'download', 'downloads', 'content', 'resources', 'public', 'public_html',
            'user', 'users', 'profile', 'profiles', 'account', 'accounts', 'member', 'members',
            'customer', 'customers', 'client', 'clients', 'partner', 'partners',
            'app', 'application', 'src', 'source', 'lib', 'libs', 'vendor', 'node_modules',
            'bower_components', 'components', 'modules', 'plugins', 'themes', 'templates',
            'cgi-bin', 'cgi-bin/php', 'cgi-bin/perl', 'cgi-bin/python', 'cgi-bin/bash',
            'icons', 'images', 'css', 'js', 'javascript', 'fonts', 'font', 'webfonts',
            'docs', 'documentation', 'doc', 'help', 'guide', 'manual', 'tutorial',
            'examples', 'sample', 'samples', 'demo', 'demos', 'test', 'tests', 'testing',
            'blog', 'news', 'shop', 'store', 'cart', 'checkout', 'payment', 'billing',
            'support', 'help', 'faq', 'forum', 'community', 'chat', 'live', 'status',
            '.well-known', '.well-known/security.txt', '.well-known/acme-challenge',
            'security', 'secure', 'ssl', 'https', 'cert', 'certs', 'certificates',
        ]
        for item in wordlist:
            self.queue.put(item)
        print(f"{self.GREEN}✅ Loaded {self.queue.qsize()} items from default wordlist{self.RESET}")

    def load_custom_wordlist(self, wordlist_path):
        try:
            if not os.path.exists(wordlist_path):
                print(f"{self.RED}❌ Wordlist file not found: {wordlist_path}{self.RESET}")
                return False
            
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                for line in lines:
                    item = line.strip()
                    if item and not item.startswith('#'):
                        self.queue.put(item)
            
            print(f"{self.GREEN}✅ Loaded {self.queue.qsize()} items from custom wordlist: {wordlist_path}{self.RESET}")
            return True
        except Exception as e:
            print(f"{self.RED}❌ Error loading wordlist: {e}{self.RESET}")
            return False

    def check_index_of(self):
        index_patterns = [
            '/index of', '/index_of', '/INDEX', '/Index of', '/Index', '/index',
            '?dir=', '?path=', '?f=', '?file=', '?folder=', '?directory=',
            '?list=', '?show=', '?view=', '?browse=', '?open=', '?read='
        ]
        
        print(f"\n{self.CYAN}🔍 Checking for directory listing vulnerabilities...{self.RESET}")
        
        for pattern in index_patterns:
            test_url = urljoin(self.target_url, pattern)
            try:
                response = self.session.get(test_url, timeout=self.timeout, allow_redirects=False)
                if response.status_code == 200:
                    if any(keyword in response.text.lower() for keyword in ['index of', 'directory listing', 'parent directory', 'name', 'last modified', 'size', 'description']):
                        with self.lock:
                            result = {
                                'url': test_url,
                                'status': response.status_code,
                                'type': 'INDEX_OF',
                                'size': len(response.content),
                                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            }
                            self.found_items.append(result)
                            self.found_count += 1
                            print(f"{self.GREEN}✓ [INDEX] {test_url}{self.RESET}")
            except:
                pass

    def check_path(self, path):
        url = urljoin(self.target_url, path)
        try:
            response = self.session.get(url, timeout=self.timeout, allow_redirects=False)
            status = response.status_code
            
            if status in [200, 201, 202, 203, 204, 301, 302, 303, 307, 308, 401, 403, 500, 503]:
                with self.lock:
                    result = {
                        'url': url,
                        'status': status,
                        'type': 'DIRECTORY' if url.endswith('/') or not '.' in path.split('/')[-1] else 'FILE',
                        'size': len(response.content),
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    self.found_items.append(result)
                    self.found_count += 1
                    
                    if status == 200:
                        color = self.GREEN
                        symbol = '✓'
                    elif status in [301, 302, 307, 308]:
                        color = self.YELLOW
                        symbol = '↪'
                    elif status == 403:
                        color = Fore.MAGENTA
                        symbol = '🔒'
                    elif status == 401:
                        color = self.RED
                        symbol = '🔐'
                    elif status in [500, 503]:
                        color = self.RED
                        symbol = '⚠'
                    else:
                        color = self.CYAN
                        symbol = '→'
                    
                    print(f"{color}{symbol} [{status}] {url}{self.RESET}")
                return True
                
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.ConnectionError:
            pass
        except:
            pass
        return False

    def worker(self):
        while True:
            try:
                path = self.queue.get(timeout=2)
                self.check_path(path)
                self.queue.task_done()
            except queue.Empty:
                break
            except:
                continue

    def scan(self):
        self.start_time = time.time()
        self.found_count = 0
        
        print(f"""
{self.CYAN}{'='*70}
🔍 EBRUTER TARGET: {self.target_url}
⚙️  THREADS: {self.threads}
⏱️  TIMEOUT: {self.timeout}s
{'='*70}{self.RESET}
        """)
        
        print(f"{self.YELLOW}📡 Checking if target is reachable...{self.RESET}")
        try:
            test_response = self.session.get(self.target_url, timeout=10)
            print(f"{self.GREEN}✅ Target reachable! Status: {test_response.status_code}{self.RESET}")
        except:
            print(f"{self.RED}❌ Target unreachable! Please check the URL.{self.RESET}")
            return None
        
        self.check_index_of()
        
        print(f"\n{self.CYAN}🚀 Starting directory scan...{self.RESET}\n")
        
        threads = []
        for _ in range(self.threads):
            t = threading.Thread(target=self.worker)
            t.daemon = True
            t.start()
            threads.append(t)
        
        self.queue.join()
        
        for t in threads:
            t.join(timeout=1)
        
        elapsed = time.time() - self.start_time
        
        return {
            'found': self.found_count,
            'time': elapsed,
            'results': self.found_items
        }

    def save_results(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("EBRUTER DIRECTORY BRUTE FORCE SCAN RESULTS\n")
            f.write("="*80 + "\n\n")
            
            f.write(f"Target URL: {self.target_url}\n")
            f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Found: {self.found_count}\n")
            f.write(f"Scan Duration: {self.time:.2f} seconds\n\n")
            
            f.write("="*80 + "\n")
            f.write("FOUND ITEMS\n")
            f.write("="*80 + "\n\n")
            
            directories = [i for i in self.results if i['type'] == 'DIRECTORY']
            files = [i for i in self.results if i['type'] == 'FILE']
            index_of = [i for i in self.results if i['type'] == 'INDEX_OF']
            
            if directories:
                f.write(f"\n📁 DIRECTORIES ({len(directories)})\n")
                f.write("-"*40 + "\n")
                for item in directories:
                    f.write(f"[{item['status']}] {item['url']}\n")
                    f.write(f"  Size: {item['size']} bytes\n")
                    f.write(f"  Time: {item['timestamp']}\n\n")
            
            if files:
                f.write(f"\n📄 FILES ({len(files)})\n")
                f.write("-"*40 + "\n")
                for item in files:
                    f.write(f"[{item['status']}] {item['url']}\n")
                    f.write(f"  Size: {item['size']} bytes\n")
                    f.write(f"  Time: {item['timestamp']}\n\n")
            
            if index_of:
                f.write(f"\n🔓 INDEX OF DIRECTORIES ({len(index_of)})\n")
                f.write("-"*40 + "\n")
                for item in index_of:
                    f.write(f"[{item['status']}] {item['url']}\n")
                    f.write(f"  Size: {item['size']} bytes\n")
                    f.write(f"  Time: {item['timestamp']}\n\n")
            
            f.write("\n" + "="*80 + "\n")
            f.write("STATUS CODE DISTRIBUTION\n")
            f.write("="*80 + "\n\n")
            
            status_counts = {}
            for item in self.results:
                status = item['status']
                status_counts[status] = status_counts.get(status, 0) + 1
            
            for code, count in sorted(status_counts.items()):
                f.write(f"  {code}: {count}\n")
            
            f.write("\n" + "="*80 + "\n")
            f.write(f"Generated by EBRUTER Directory Scanner Tool\n")
            f.write(f"Developer: @ERROR0101risback\n")
            f.write("="*80 + "\n")
        
        print(f"\n{self.GREEN}✅ Results saved to: {filename}{self.RESET}")
        return filename

def show_menu():
    print(f"""
{Fore.CYAN}{'='*70}
{Fore.YELLOW}🔍 EBRUTER - ADVANCED DIRECTORY BRUTE FORCE TOOL
{Fore.CYAN}Find: directories • files • admin panels • backups • configs • databases
{Fore.CYAN}{'='*70}{Style.RESET_ALL}
    """)
    
    print(f"{Fore.RED}⚠️  DISCLAIMER:{Style.RESET_ALL}")
    print(f"   This tool is for {Fore.YELLOW}EDUCATIONAL PURPOSES{Style.RESET_ALL} and {Fore.YELLOW}AUTHORIZED{Style.RESET_ALL}")
    print(f"   security testing ONLY. Scanning websites without permission")
    print(f"   is ILLEGAL. Use responsibly.\n")
    
    print(f"{Fore.GREEN}📋 SELECT WORDLIST MODE:{Style.RESET_ALL}")
    print(f"   {Fore.CYAN}[1]{Style.RESET_ALL} Default Wordlist (400+ common directories)")
    print(f"   {Fore.CYAN}[2]{Style.RESET_ALL} Custom Wordlist (Load your own file)")
    print()
    
    choice = input(f"{Fore.GREEN}👉 Enter your choice (1 or 2): {Style.RESET_ALL}").strip()
    
    while choice not in ['1', '2']:
        print(f"{Fore.RED}❌ Invalid choice! Please enter 1 or 2{Style.RESET_ALL}")
        choice = input(f"{Fore.GREEN}👉 Enter your choice (1 or 2): {Style.RESET_ALL}").strip()
    
    return choice

def main():
    try:
        choice = show_menu()
        
        url = input(f"{Fore.GREEN}🌐 Enter website URL (e.g., example.com): {Style.RESET_ALL}").strip()
        if not url:
            print(f"{Fore.RED}❌ No URL provided!{Style.RESET_ALL}")
            return
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        threads_input = input(f"{Fore.GREEN}⚙️  Number of threads (default 50): {Style.RESET_ALL}").strip()
        threads = int(threads_input) if threads_input.isdigit() else 50
        
        timeout_input = input(f"{Fore.GREEN}⏱️  Request timeout in seconds (default 5): {Style.RESET_ALL}").strip()
        timeout = int(timeout_input) if timeout_input.isdigit() else 5
        
        scanner = EbruterScanner(url, threads, timeout)
        
        if choice == '1':
            scanner.load_default_wordlist()
        else:
            wordlist_path = input(f"{Fore.GREEN}📂 Enter path to wordlist file: {Style.RESET_ALL}").strip()
            if not wordlist_path:
                print(f"{Fore.RED}❌ No wordlist path provided!{Style.RESET_ALL}")
                return
            if not scanner.load_custom_wordlist(wordlist_path):
                return
        
        results = scanner.scan()
        
        if not results:
            return
        
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✅ SCAN COMPLETE!{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"📊 Found: {Fore.GREEN}{results['found']}{Style.RESET_ALL} items")
        print(f"⏱️  Time: {Fore.YELLOW}{results['time']:.2f}{Style.RESET_ALL} seconds")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        if results['found'] > 0:
            filename = input(f"{Fore.GREEN}💾 Enter filename to save results (default: scan_results.txt): {Style.RESET_ALL}").strip()
            if not filename:
                filename = f"ebruter_scan_{int(time.time())}.txt"
            if not filename.endswith('.txt'):
                filename += '.txt'
            
            scanner.results = results['results']
            scanner.time = results['time']
            scanner.save_results(filename)
        else:
            print(f"{Fore.YELLOW}📭 No directories or files found.{Style.RESET_ALL}")
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.RED}⚠️ Scan interrupted by user{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}👋 Scan completed. Use responsibly!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()