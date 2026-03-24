# ⚡ **EBRUTER - Advanced Directory Brute Force Tool**

### *Web Directory & File Discovery Tool for Security Professionals*

<div align="center">
  <img src="https://iili.io/qEHckKv.webp" alt="EBRUTER Logo" width="250"/>
  
  [![Version](https://img.shields.io/badge/version-1.0-red.svg)]()
  [![Python](https://img.shields.io/badge/python-3.7+-blue.svg)]()
  [![License](https://img.shields.io/badge/license-Educational%20Only-orange.svg)]()
  
  [![Telegram](https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/ERROR0101risback)
  [![Instagram](https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=for-the-badge&logo=instagram)](https://instagram.com/fahad0101r)
  [![GitHub](https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=for-the-badge&logo=github)](https://github.com/ERROR0101r)
  [![Telegram Channel](https://img.shields.io/badge/Channel-@aab_ho_ga_comeback-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/aab_ho_ga_comeback)
  
  <p><strong>Developer: @ERROR0101risback</strong></p>
</div>

---

## 📋 **TABLE OF CONTENTS**
- [📌 What is EBRUTER?](#-what-is-ebruter)
- [⚠️ STRICT DISCLAIMER](#️-strict-disclaimer)
- [🎯 What It Finds](#-what-it-finds)
- [🚀 Features](#-features)
- [📁 File Structure](#-file-structure)
- [📦 Installation](#-installation)
- [🔧 Usage](#-usage)
- [💻 Commands](#-commands)
- [📊 Output File Format](#-output-file-format)
- [🎯 Example Run](#-example-run)
- [👨‍💻 Developer](#-developer)
- [⚖️ Legal Notice](#️-legal-notice)

---

## 📌 **WHAT IS EBRUTER?**

**EBRUTER** is an advanced directory brute force tool designed for **security professionals, penetration testers, and ethical hackers**. It systematically discovers hidden directories, files, admin panels, backup files, configuration files, and database dumps on web servers.

The tool uses intelligent wordlist-based scanning with multi-threading to efficiently uncover exposed resources that should not be publicly accessible.

---

## ⚠️ **STRICT DISCLAIMER**

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   ⚠️  THIS TOOL IS FOR EDUCATIONAL AND AUTHORIZED SECURITY TESTING ONLY  ║
║                                                                           ║
║   • Unauthorized scanning of websites you do not own is ILLEGAL          ║
║   • This tool violates computer fraud laws in most countries             ║
║   • Use only on systems you OWN or have EXPLICIT WRITTEN PERMISSION      ║
║   • The developer assumes NO LIABILITY for misuse                         ║
║   • You are SOLELY RESPONSIBLE for your actions                          ║
║                                                                           ║
║   By using this tool, you confirm:                                        ║
║   ✓ You have permission to test the target                                ║
║   ✓ You understand the legal implications                                 ║
║   ✓ You accept full responsibility for any consequences                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

## 🎯 **WHAT IT FINDS**

| Category | Examples |
|----------|----------|
| **Admin Panels** | `/admin`, `/wp-admin`, `/cpanel`, `/phpmyadmin` |
| **Backup Files** | `backup.zip`, `database.sql`, `config.php.bak` |
| **Configuration** | `.env`, `wp-config.php`, `config.php`, `.git/config` |
| **Sensitive Files** | `robots.txt`, `.htaccess`, `phpinfo.php` |
| **Upload Directories** | `/uploads`, `/files`, `/images` |
| **API Endpoints** | `/api/v1`, `/graphql`, `/swagger` |
| **Development Files** | `.git/`, `.svn/`, `composer.json`, `package.json` |
| **Directory Listings** | Index of / (open directory vulnerabilities) |

---

## 🚀 **FEATURES**

| Feature | Description |
|---------|-------------|
| ✅ **Multi-threaded scanning** | Configurable thread count for faster scans |
| ✅ **Default wordlist** | 8000+ common directories and paths |
| ✅ **Custom wordlist support** | Use your own wordlists |
| ✅ **Directory listing detection** | Finds open indexes |
| ✅ **Status code tracking** | 200, 301, 403, 401, 500 detection |
| ✅ **Color-coded output** | Easy reading in terminal |
| ✅ **Save results** | Export to text file |
| ✅ **Auto-install** | Dependencies install automatically |
| ✅ **Cross-platform** | Termux, Linux, Windows |

---

## 📁 **FILE STRUCTURE**

```
Ebruter/
│
├── Ebruter.py            # Main Python tool
├── drlist.txt            # Default wordlist (8000+ entries)
├── setup.sh              # Auto-installer script
└── README.md             # Documentation
```

### **Wordlist Information**

`drlist.txt` contains **8000+** directory names and paths including:
- Common admin panels
- Backup file names
- Configuration files
- Development directories
- API endpoints
- Sensitive file paths

You can also use your own custom wordlist with the tool.

---

## 📦 **INSTALLATION**

### **Termux (Android):**
```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/ERROR0101r/Ebruter.git
cd Ebruter
chmod +x setup.sh
./setup.sh
```

### **Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip git
git clone https://github.com/ERROR0101r/Ebruter.git
cd Ebruter
pip3 install requests colorama
```

### **Windows:**
```bash
git clone https://github.com/ERROR0101r/Ebruter.git
cd Ebruter
pip install requests colorama
python Ebruter.py
```

---

## 🔧 **USAGE**

### **Run the tool:**
```bash
python3 Ebruter.py
```

### **Menu Options:**

```
╔══════════════════════════════════════════════════════════╗
║                    EBRUTER v1.0                          ║
║              Directory Brute Force Tool                  ║
╚══════════════════════════════════════════════════════════╝

Select wordlist:
1. Default Wordlist (8000+ common directories)
2. Custom Wordlist (load your own file)

Enter choice (1/2):
```

### **After selection, enter:**
1. Target URL (e.g., `example.com` or `https://example.com`)
2. Number of threads (default: 50)
3. Request timeout (default: 5 seconds)

---

## 💻 **COMMANDS**

| Command | Description |
|---------|-------------|
| `python3 Ebruter.py` | Run the tool |
| `Ctrl + C` | Stop scan |
| Default save | `ebruter_scan_[timestamp].txt` |

---

## 📊 **OUTPUT FILE FORMAT**

Results are saved with:

```
╔══════════════════════════════════════════════════════════╗
║           EBRUTER SCAN REPORT                           ║
╠══════════════════════════════════════════════════════════╣
║ Target: https://example.com                             ║
║ Scan Date: 2026-03-24 15:30:45                          ║
║ Wordlist: drlist.txt (8000+ entries)                    ║
║ Threads: 50                                             ║
║ Timeout: 5 seconds                                      ║
╠══════════════════════════════════════════════════════════╣
║                       FINDINGS                          ║
╠══════════════════════════════════════════════════════════╣
║ [200] https://example.com/admin                         ║
║ [301] https://example.com/wp-admin                      ║
║ [200] https://example.com/robots.txt                    ║
║ [403] https://example.com/.git                          ║
║ [200] https://example.com/backup.zip                    ║
║ [401] https://example.com/phpmyadmin                    ║
╠══════════════════════════════════════════════════════════╣
║                      SUMMARY                            ║
╠══════════════════════════════════════════════════════════╣
║ Total Found: 24                                         ║
║ 200 OK: 8                                               ║
║ 301 Redirect: 5                                         ║
║ 403 Forbidden: 6                                        ║
║ 401 Unauthorized: 3                                     ║
║ 500 Internal: 2                                         ║
║ Scan Time: 45.23 seconds                                ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🎯 **EXAMPLE RUN**

```
🌐 Enter website URL: example.com
⚙️ Number of threads (default 50): 50
⏱️ Request timeout in seconds (default 5): 5

🚀 Starting directory scan...

✓ [200] https://example.com/admin
↪ [301] https://example.com/wp-admin
✓ [200] https://example.com/robots.txt
🔒 [403] https://example.com/.git
✓ [200] https://example.com/backup.zip
🔐 [401] https://example.com/phpmyadmin
✓ [200] https://example.com/uploads
↪ [301] https://example.com/api
🔒 [403] https://example.com/.env
✓ [200] https://example.com/config.php

✅ SCAN COMPLETE!
📊 Found: 24 items
⏱️ Time: 45.23 seconds

💾 Enter filename (press Enter for default): scan_results.txt
✅ Results saved to: scan_results.txt
```

---

## 📊 **STATUS CODE MEANINGS**

| Code | Meaning | Description |
|------|---------|-------------|
| **200** | OK | Directory/file exists and is accessible |
| **301** | Redirect | Moved permanently |
| **302** | Found | Temporary redirect |
| **403** | Forbidden | Exists but access denied |
| **401** | Unauthorized | Requires authentication |
| **404** | Not Found | Does not exist (not shown in results) |
| **500** | Internal Error | Server error |

---

## 🛠️ **CUSTOM WORDLIST FORMAT**

To use a custom wordlist, create a text file with one path per line:

```
admin
wp-admin
phpmyadmin
backup.zip
config.php
.env
.git/config
uploads
api/v1
```

Save it as any filename and select option 2 when running the tool.

---

## 👨‍💻 **DEVELOPER**

<div align="center">
  <table>
    <tr>
      <td align="right"><strong>Name:</strong>    </td>
      <td><code>ERROR0101risback / Fahad</code></td>
    </tr>
    <tr>
      <td align="right"><strong>Telegram:</strong>    </td>
      <td><a href="https://t.me/ERROR0101risback">@ERROR0101risback</a></td>
    </tr>
    <tr>
      <td align="right"><strong>Instagram:</strong>    </td>
      <td><a href="https://instagram.com/fahad0101r">@fahad0101r</a></td>
    </tr>
    <tr>
      <td align="right"><strong>Telegram Channel:</strong>    </td>
      <td><a href="https://t.me/aab_ho_ga_comeback">@aab_ho_ga_comeback</a></td>
    </tr>
    <tr>
      <td align="right"><strong>GitHub Profile:</strong>    </td>
      <td><a href="https://github.com/ERROR0101r">ERROR0101r</a></td>
    </tr>
    <tr>
      <td align="right"><strong>Project Repo:</strong>    </td>
      <td><a href="https://github.com/ERROR0101r/Ebruter">Ebruter</a></td>
    </tr>
    <tr>
      <td align="right"><strong>Version:</strong>    </td>
      <td>1.0</td>
    </tr>
  </table>
</div>

---

## ⭐ **SUPPORT THE PROJECT**

If you find EBRUTER useful for authorized security testing:
- ⭐ **Star** the repository on [GitHub](https://github.com/ERROR0101r/Ebruter)
- 📢 **Share** with security professionals
- 📝 **Join** the [Telegram Channel](https://t.me/aab_ho_ga_comeback)
- 👤 **Follow** on [Instagram](https://instagram.com/fahad0101r)
- 🐛 **Report bugs** to help improve the tool

---

## 📥 **DIRECT DOWNLOAD**

**Download ZIP:**
```
https://github.com/ERROR0101r/Ebruter/archive/refs/heads/main.zip
```

---

## ⚖️ **LEGAL NOTICE**

```
This tool is intended for:

✓ Educational purposes
✓ Authorized penetration testing
✓ Security research with permission

The developer does not condone or support:

✗ Unauthorized access to systems
✗ Illegal activities
✗ Malicious use

USE RESPONSIBLY. STAY LEGAL.
```

---

<div align="center">
  <h3>⚡ Discover. Test. Secure. ⚡</h3>
  <p><i>Made with 🔥 by @ERROR0101risback</i></p>
  
  <p>
    <a href="https://t.me/ERROR0101risback"><img src="https://img.shields.io/badge/Telegram-@ERROR0101risback-26A5E4?style=flat-square&logo=telegram" alt="Telegram"></a>
    <a href="https://instagram.com/fahad0101r"><img src="https://img.shields.io/badge/Instagram-@fahad0101r-E4405F?style=flat-square&logo=instagram" alt="Instagram"></a>
    <a href="https://github.com/ERROR0101r"><img src="https://img.shields.io/badge/GitHub-ERROR0101r-181717?style=flat-square&logo=github" alt="GitHub"></a>
    <a href="https://t.me/aab_ho_ga_comeback"><img src="https://img.shields.io/badge/Channel-@aab_ho_ga_comeback-2CA5E0?style=flat-square&logo=telegram" alt="Channel"></a>
    <a href="https://github.com/ERROR0101r/Ebruter/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/Download-ZIP-brightgreen?style=flat-square&logo=github" alt="Download"></a>
  </p>
  
  <p>© 2026 EBRUTER. All rights reserved.</p>
</div>