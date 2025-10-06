import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("db", "scans.db")

def init_db():
    """initialize the database and create tables if they don't exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            open_ports TEXT,
            vulnerabilities TEXT,
            firewall_issues TEXT,
            password_issues TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_scan(ip, open_ports, vulnerabilities=None, firewall_issues=None, password_issues=None):
    """save a scan record into the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO scans (ip, timestamp, open_ports, vulnerabilities, firewall_issues, password_issues)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        ip,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ",".join(map(str, open_ports)) if open_ports else "",
        "\n".join(vulnerabilities) if vulnerabilities else "",
        "\n".join(firewall_issues) if firewall_issues else "",
        "\n".join(password_issues) if password_issues else ""
    ))
    conn.commit()
    conn.close()

def get_scans(limit=10):
    """fetch the most recent scans"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
