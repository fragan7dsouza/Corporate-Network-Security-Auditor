# 🛡️ Corporate Network Security Auditor (CNSA)

A lightweight Python-based security auditing tool to scan networks, detect vulnerabilities, and evaluate firewall and password policies. Built with modular architecture, database logging, and optional Flask-based UI for managing reports.  

---

## ⚙️ Features

- ✅ Port scanning (detect open & risky ports)  
- ✅ Vulnerability detection for common services  
- ✅ Firewall rule analysis (basic misconfigurations)  
- ✅ Password policy audit (weak password detection)  
- ✅ Report generation (text format)  
- ✅ Database integration (SQLite for storing scans)  
- ✅ Flask-based dashboard UI to view scan history  

---

## 📁 Project Structure

```
CNSA/
│
├── main.py                    # entry point (CLI menu for scans)
├── auditor.py                 # full audit runner
│
├── scanner/                   # scanning modules
│   ├── port_scanner.py        # uses nmap/socket to detect open ports
│   ├── vuln_scanner.py        # check weak services / CVEs
│   └── firewall_check.py      # basic firewall misconfig detection
│
├── auth/                      # authentication checks
│   └── password_policy.py     # password strength auditing
│
├── reports/                   # reporting system
│   └── report_writer.py       # generates TXT reports
│
├── db/                        # database layer
│   └── database.py            # SQLite integration for scan storage
│
├── ui/                        # web dashboard (Flask)
│   ├── app.py                 # flask app entry
│   └── templates/
│       └── dashboard.html     # UI for viewing scan results
│
├── utils/                     # helper functions
│   └── logger.py              # centralized logging
│
├── config/
│   └── settings.json          # global config
│
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed  
- Install dependencies using pip:

```bash
pip install -r requirements.txt
```

---

### 🖱️ How to Run

1. **Run via CLI (Menu-based interface):**

```bash
python main.py
```

2. **Run a Full Audit directly:**

```bash
python auditor.py
```

3. **Run the Web Dashboard (Flask UI):**

```bash
python ui/app.py
```

Then open in browser:

```
http://127.0.0.1:5000/
```

---

## 📄 Reports & Database

- All scan reports are stored in the `reports/` folder (`.txt` format).  
- Scan history is logged into an SQLite database: `db/scans.db`.  
- You can view recent scans with the script:

```bash
python view_scans.py
```

---

## 📌 Notes

- This tool is for **educational & research purposes only**.  
- Run with proper permissions (admin/sudo may be required for network scans).  

---

## 👨‍💻 Author

**Fragan Dsouza**  
📎 [LinkedIn](https://www.linkedin.com/in/fragan-d-souza-64626a29b)  
💻 [GitHub](https://github.com/fragan7dsouza)

---

## 📜 License

This project is open-source and free to use under the MIT License.


