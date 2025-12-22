# 🔱 SQLijin v2.1
*Advanced SQLi Reconnaissance & Passive Vulnerability Fingerprinter*

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-lightgrey.svg)](https://www.linux.org/)

SQLijin is an elite-grade reconnaissance tool designed for Bug Bounty hunters and Security Evaluators. It leverages Google’s massive search index to passively discover attack surfaces across entire domains and subdomains, identifying live parameters and flagging high-confidence SQL injection leaks before you ever send a heavy payload.

---

## Key Features (v2.1 Elite)
* *Wildcard Subdomain Sweeping:* Targeted recon using *.target.com to find hidden legacy assets.
* *Passive Fingerprinting:* Identifies "Confirmed Leaks" by detecting database error strings in page responses.
* *Elite CLI Interface:* Powered by Rich and Pyfiglet with red hacker-themed banners and interactive progress bars.
* *Timestamped Auditing:* Auto-creates unique session folders for every audit to maintain clean logs.
* *Live Status Verification:* Filters out dead links (404s) to ensure you only test active targets.

---

## Installation & Private Environment Setup

Running in a *Virtual Environment (venv)* is highly recommended. This creates a "private sandbox" so the tool's dependencies don't interfere with your system's Python settings.

### 1. Clone & Setup
```bash
# Clone the repository
git clone [https://github.com/G33l0/SQLijin.git](https://github.com/G33l0/SQLijin.git)
cd SQLijin

# Create a private virtual environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate

2. Automated Install
While inside your active virtual environment, run the installer:
chmod +x install.sh
./install.sh

 Usage
 * Configure Target: Open SQLijin.py and set the TARGET_SCOPE (e.g., *.bugcrowd.com).
 * Add Dorks: Ensure your dorks.txt is populated with the provided high-grade patterns.
 * Launch:
   python3 SQLijin.py

Interactive CLI Map
 Bug Bounty Workflow
This tool is optimized for the "Passive Recon" phase of a Bug Bounty (Bugcrowd/HackerOne):
 * Discovery: Use SQLijin to find indexed subdomains and parameters.
 * Validation: Review CRITICAL_VULNS.txt in your timestamped session folder.
 * PoC: Feed confirmed URLs into sqlmap for the final Proof of Concept.
   sqlmap -u "FOUND_URL" --batch --banner

 Session Management
SQLijin automatically organizes your work:
 * bounty_[domain]_[timestamp]/
   * all_urls.txt: Every live URL discovered.
   * CRITICAL_VULNS.txt: Targeted URLs that leaked database errors.
 Legal Disclaimer
FOR AUTHORIZED USE ONLY. This tool is for educational purposes and authorized security evaluations. The maker (@x0x0h33l0) is not responsible for misuse or any illegal activity. Always respect the Rules of Engagement for Bug Bounty programs.
Maker: https://t.me/x0x0h33l0

---

### Final Tip for Your Linux VM
When you are done using the tool, you can simply type deactivate in your terminal to close the private environment. Next time you want to use the tool, just navigate back to the folder and run source venv/bin/activate.