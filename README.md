# 🌐 Proxies: Continuously Updated Proxy Lists

## 👋 Welcome to Proxies!

This repository serves as a **dynamic and regularly updated source of free HTTP, SOCKS4, and SOCKS5 proxies**. The primary goal of this project is to provide a fresh list of proxies for various uses while also keeping my GitHub contribution graph consistently green through automated updates.

***

## ✨ How It Works

This project leverages **GitHub Actions** to automate the process of fetching, consolidating, and updating proxy lists:

1. **Source Aggregation**: The `update_proxies.py` script, hidden from direct view, regularly fetches raw proxy data from several trusted open-source GitHub repositories.  
2. **Deduplication & Sorting**: All collected proxies are combined into a single dataset. Duplicates are automatically removed, and the list is then sorted for consistency and ease of use.  
3. **Categorized Output**: The script then organizes these unique proxies into separate files based on their type (HTTP, SOCKS4, SOCKS5) and generates a consolidated file with all available proxies.  
4. **Automated Commits**: Every **30 minutes**, a GitHub Action runs the script. If any changes are detected in the proxy lists, a new commit is automatically pushed to this repository, ensuring the lists are always up-to-date.  

***

## 📦 Output Files

You'll find the following updated proxy list files in the `proxies/` directory:

- `proxies/all_proxies.txt`: A comprehensive, deduplicated, and sorted list of all available proxies (HTTP, SOCKS4, SOCKS5).  
- `proxies/http.txt`: A list of unique HTTP proxies.  
- `proxies/socks4.txt`: A list of unique SOCKS4 proxies.  
- `proxies/socks5.txt`: A list of unique SOCKS5 proxies.  

These files are updated automatically every **30 minutes**.

***

## 🚀 Usage

You can easily use these proxy lists in your applications or scripts. The simplest way is to download them directly using a command-line tool like `curl`.

### **Download Proxy Lists via `curl`**

Simply copy and paste the command for the list you need.

**Download All Proxies:**
```bash
curl -o all_proxies.txt https://raw.githubusercontent.com/Ian-Lusule/Proxies/main/proxies/all_proxies.txt
```

**Download HTTP Proxies:**
```bash
curl -o http.txt https://raw.githubusercontent.com/Ian-Lusule/Proxies/main/proxies/http.txt
```

**Download SOCKS4 Proxies:**
```bash
curl -o socks4.txt https://raw.githubusercontent.com/Ian-Lusule/Proxies/main/proxies/socks4.txt
```

**Download SOCKS5 Proxies:**
```bash
curl -o socks5.txt https://raw.githubusercontent.com/Ian-Lusule/Proxies/main/proxies/socks5.txt
```

-----

## 👤 About

This project is maintained by **Ian Lusule** ([@Ian-Lusule](https://github.com/Ian-Lusule)).

Feel free to ⭐ this repository if you find it useful! ✨
