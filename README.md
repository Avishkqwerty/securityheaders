# securityheaders
Check the Security Headers
Security Header Checker by Sri Lanka CERT
Security Header Check
A simple and effective tool to check HTTP security headers.
🚀 Overview
Security Header Check is a Python-based tool that helps security professionals and web developers analyze the presence of essential security headers in a website's HTTP response. It identifies missing security headers that could expose a website to potential attacks.
This tool is officially used for auditing security headers and ensuring compliance with best security practices.
🔥 Features
✅ Checks for critical security headers, including:
Strict-Transport-Security (HSTS)
Content-Security-Policy (CSP)
X-Content-Type-Options
X-Frame-Options
X-XSS-Protection
Referrer-Policy
Feature-Policy (Deprecated, but checked for legacy systems)
Permissions-Policy (Replaces Feature-Policy)
✅ Provides a clear report of existing and missing security headers
✅ Supports interactive scanning, allowing users to check multiple domains
✅ Fast and lightweight, requiring only Python and minimal dependencies
🛠️ Requirements
Ensure you have the following installed before running the tool:
Python 3.x (Recommended: Python 3.7 or later)
Required Python libraries:
requests (for sending HTTP requests)
termcolor (for colored terminal output)
🔧 Installation
1️⃣ Install Python
Ensure Python 3 is installed on your system:
python3 --version
 
Alternatively, install them manually:
pip3 install requests termcolor
🚀 Usage
Run the tool using:
python3 headertool.py
How It Works
1️⃣ Enter a domain (e.g., example.com) when prompted.
2️⃣ The tool checks security headers and displays the results.
3️⃣ After the check, it asks if you want to analyze another domain.
Example Output
🔹 Enter the domain (e.g., example.com): example.com
✅ Existing Security Headers:
  - Strict-Transport-Security
  - Content-Security-Policy
  - X-Frame-Options
❌ Missing Security Headers:
  - X-Content-Type-Options
  - Referrer-Policy
  - Permissions-Policy
🔄 Do you want to check another domain? (y/n):
🎯 Why Use This Tool?
🔹 Improves Website Security – Helps web administrators enforce best practices.
🔹 Easy to Use – Just enter a domain and get instant results.
🔹 Lightweight & Fast – No heavy dependencies or setup required.
🔹 Helps with Compliance – Ensures adherence to security standards like OWASP, GDPR, etc.
🤝 Contributing
Contributions are welcome! Feel free to:
Open an issue for feature requests or bug reports.
Fork the repo and submit a pull request.


