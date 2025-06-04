File Integrity Checker 
This project is a File Integrity Checker that monitors files for unauthorized changes using cryptographic hashing (SHA-256). It consists of a Python Flask backend and a web-based frontend.

📌 Features
✅ Scan Files - Record file hashes for later comparison.
✅ Detect Changes - Check if files have been modified, deleted, or added.
✅ Simple Web Interface - Easy-to-use dashboard for scanning and checking.
✅ Real-time Alerts - Highlights modified/new files.

⚙️ Setup & Installation
1. Prerequisites
Python 3.6+

Flask (pip install flask)

Web browser (Chrome/Firefox)

2. Clone the Repository
sh
git clone [https://github.com/your-repo/file-integrity-checker.git](https://github.com/sumit3162/File-Integrity-Checker)
cd file-integrity-checker
3. Run the Backend (Flask Server)
sh
python integrity_checker.py
Note: The server runs at http://localhost:5000.

4. Open the Frontend
Open index.html in a browser (or use a local HTTP server like python -m http.server 8000).

🖥️ Usage
1. Scan a Directory
Enter a directory path (e.g., ./test_files).

Click "Scan Files" to generate baseline hashes.

2. Check for Changes
Click "Check Integrity" to compare current files with the baseline.

Modified files appear in red, new files in blue.

📂 Example Directory Structure
project/
│── integrity_checker.py (Backend)
│── index.html (Frontend)
└── test_files/ (Sample files to monitor)
    ├── file1.txt
    ├── file2.log
    └── config.json
🔧 Possible Improvements
Database Storage: Use SQLite/PostgreSQL instead of in-memory storage.

Scheduled Scans: Automate checks with cron or Celery.

Email Alerts: Send notifications when changes are detected.

User Authentication: Secure access with login.

⚠️ Security Notes
Do not expose the Flask server publicly (use only in trusted networks).

Store hashes securely (encrypt if sensitive).

📜 License
MIT License - Free for personal and commercial use.
