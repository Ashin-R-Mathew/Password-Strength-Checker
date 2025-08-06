# 🔐 Password Strength Checker

A Python-based terminal application to check the strength of a password based on multiple security metrics.  
It analyzes passwords for length, character diversity, common patterns, dictionary usage, and more.

---

## 🚀 Features

- Checks for:
  - ✅ Length and complexity
  - 🔡 Uppercase, lowercase, numbers, and special characters
  - ❌ Repeated number sequences (e.g., `111`, `123123`)
  - ⚠️ Common numeric patterns (e.g., `123`, `9876`)
  - 📃 Passwords from common password list
- Rates password on a scale of **0 to 10**
- Provides **clear strength label** and **suggestions to improve**
- Designed with **readability and extensibility** in mind

---

## 🛠 Requirements

- Python 3.6 or higher

No external packages are required — only standard Python libraries (`string`, `re`).

---

## 🧪 Usage

1. Clone the repository or download the script.
2. Ensure `common.txt` (see below) is placed in the same directory.
3. Run the program:
   ```bash
   python3 main.py
4. Enter your password when prompted.

## ⚠️ Important: Common Password List
To ensure accurate checking against weak and frequently used passwords, you must download the common.txt file:

📥 Download Link:
[Download common.txt](https://drive.google.com/file/d/1jM0aTaAWETK8-jtj4-BdIo8uvuMEmBXv/view?usp=sharing)

After downloading:

- Place the file in the same directory as main.py.

## License 📜
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. ⚖️
