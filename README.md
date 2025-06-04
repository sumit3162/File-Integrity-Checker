

---

````markdown
# 🛡️ File Integrity Checker

![Python](https://img.shields.io/badge/Built%20with-Python%203-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightblue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![UI](https://img.shields.io/badge/UI-HTML%2FCSS-orange)

A lightweight web-based tool to scan directories and monitor file integrity using hash comparisons. Useful for detecting unauthorized file changes and maintaining system security.

## 🖼️ Project Preview

<img src="https://raw.githubusercontent.com/yourusername/yourrepo/main/demo.png" alt="App Screenshot" width="700"/>

> Replace `yourusername/yourrepo` with your actual GitHub repo path and upload a screenshot named `demo.png`.

---

## 🔧 Features

- ✅ Scan a directory and store file hashes (SHA-256)
- ✅ Detect modified or newly added files
- ✅ Simple, responsive web interface
- ✅ Fast, real-time responses via Flask backend

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/file-integrity-checker.git
cd file-integrity-checker
````

### 2. Install Dependencies

```bash
pip install flask
```

### 3. Run the Application

```bash
python integrity_checker.py
```

The app will start at `http://localhost:5000`.

### 4. Open `index.html`

You can open `index.html` directly in a browser or serve it with a simple HTTP server.

---

## 📁 Project Structure

```
├── index.html              # Frontend interface
├── integrity_checker.py    # Flask backend with hashing logic
└── README.md               # You're reading it!
```

---

## 📸 Screenshots

| 📂 Scan Files                                                                  | 🔍 Check Integrity                                                               |
| ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| ![Scan](https://raw.githubusercontent.com/yourusername/yourrepo/main/scan.png) | ![Check](https://raw.githubusercontent.com/yourusername/yourrepo/main/check.png) |

---

## ⚠️ Notes

* This version stores hashes **in memory** (non-persistent). Restarting the server resets the scanned data.
* To make it production-ready, integrate a **database** like SQLite or MongoDB to persist hashes.

---

## 💡 Future Enhancements

* Add email notifications on modification
* Persistent database support
* User authentication
* Command-line interface (CLI)

---

## 🤝 Contributing

Pull requests are welcome! If you have suggestions or find bugs, please open an issue.

---

## 📜 License

MIT License © 2025 Sumit Shingane

---

```


