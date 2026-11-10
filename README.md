# Web - XSS Payload Generator and Obfuscator

## 📌 Project Overview
The **Web - XSS Payload Generator and Obfuscator** is a modular, offline Python tool designed for authorized web vulnerability testing. It automates the generation and obfuscation of Cross-Site Scripting (XSS) payloads to assist security researchers and penetration testers in bypassing basic web filters during authorized security assessments.

This tool was developed as a group project focusing on Web Application Attacks, emphasizing ethical coding practices, modular architecture, and secure data handling.

## ⚠️ Legal Disclaimer & Ethical Guidelines
**Compliance:** This tool is developed strictly for educational purposes and authorized penetration testing only. 

Users must ensure compliance with the **Malaysia Computer Crimes Act 1997** (or applicable local laws). 
* Any unauthorized use of these payloads against third-party systems, networks, or applications is strictly prohibited and illegal.
* The developers of this tool assume no liability for misuse or damage caused by this software.

### Rules of Engagement (RoE)
1. **Authorization:** Only use this tool against applications where explicit, written consent has been granted by the owner.
2. **Safe Defaults:** This tool does not establish any network connections. All payload generations and conversions happen locally on the host machine.
3. **Data Handling:** Generated payloads are saved locally to an `output/` directory and are not transmitted externally.

## 🛠️ Features & Encoding Engine
This tool takes a base XSS payload (e.g., `<script>alert(1)</script>`) and automatically generates three obfuscated variations to test different input validation filters:
* **URL Encoding:** Converts special characters to `%xx` format for testing URL-based injection points.
* **Base64 Encoding:** Encodes the payload into Base64 format for testing applications that decode base64 inputs.
* **HTML Entity Encoding:** Converts characters like `<` and `>` into HTML entities to bypass basic WAFs (Web Application Firewalls).

## 🗂️ Modular Architecture
The project is built using standard Python libraries and divided into 5 distinct modules for clean code management and team collaboration:
* `main.py` - Core execution loop and module integration.
* `encoders.py` - The encoding engine (URL, Base64, HTML).
* `ethics.py` - Enforces the legal disclaimer and authorization kill-switch.
* `storage.py` - Handles "Safe Defaults" by saving outputs locally to `.txt` files.
* `ui.py` - Terminal interface and visual formatting.

## 🚀 Installation & Usage

**Prerequisites:** Python 3.x installed (No external libraries required).

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
   cd YOUR_REPOSITORY_NAME

2. Run the application:
   ```bash
   python main.py
   (Note: Linux/macOS users may need to use python3 main.py)

3. Follow the on-screen prompts to authorize the session and input your base payloads. Check the output/payloads.txt file for your generated results.


## 👥 Contributors
* **Nur Amirah Binti Roslan (52215125785)** - Core Engine & Integration (`main.py`)
* **Isyraf Bin Salahuddin (52215225140)** - Encoding Engine (`encoders.py`)
* **Omar Asraf Bin Kader Mohideen (52215125977)** - Ethical Guardrails & Compliance (`ethics.py`)
* **Muhammad Afnan Danish Bin Mohd Alfanizan (52215125101)** - Data Handling & Storage (`storage.py`)
* **Muhammad Arif Azim Bin Md Adha (52215125602)** - UI Design & Repository Manager (`ui.py`)



