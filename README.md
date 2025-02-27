# 🔒 Security Header Check  

A simple and efficient tool to analyze HTTP security headers and identify missing ones to enhance web security.

## 🚀 Overview  
**Security Header Check** is a Python-based tool designed for security professionals and web developers. It checks the HTTP response headers of a given website and reports missing security headers. This ensures websites comply with security best practices and remain protected against common web attacks.

---

## 🔥 Features  
✅ **Analyzes critical security headers**, including:  
- Strict-Transport-Security (HSTS)  
- Content-Security-Policy (CSP)  
- X-Content-Type-Options  
- X-Frame-Options  
- X-XSS-Protection  
- Referrer-Policy  
- Feature-Policy *(for legacy support)*  
- Permissions-Policy *(modern replacement for Feature-Policy)*  

✅ **Provides a detailed report** of existing and missing security headers  
✅ **Interactive mode** for checking multiple domains  
✅ **Lightweight and easy to use**  

---

## 🛠️ Requirements  
Before running the tool, ensure you have the following installed:  
- **Python 3.x** (Recommended: Python 3.7 or later)  
- Required Python libraries:  
  - `requests` *(for sending HTTP requests)*  
  - `termcolor` *(for colored terminal output)*  

---

## 🔧 Installation  

### **1️⃣ Install Python**  
Check if Python is installed:  
```bash
python3 --version

If not installed, download it from python.org.

2️⃣ Clone the Repository
git clone https://github.com/Avishkqwerty/securityheaders
'cd security-header-check'

3️⃣ Install Dependencies
Run the following command to install required libraries:
'pip install requests termcolor'

How It Works
1️⃣ Enter a domain (e.g., example.com) when prompted.
2️⃣ The tool scans the domain's security headers and displays the results.
3️⃣ After the check, you can scan another domain or exit.

🔹 Enter the domain (e.g., example.com): example.com

✅ Existing Security Headers:
  - Strict-Transport-Security
  - Content-Security-Policy
  - X-Frame-Options

❌ Missing Security Headers:
  - X-Content-Type-Options
  - Referrer-Policy
  - Permissions-Policy





