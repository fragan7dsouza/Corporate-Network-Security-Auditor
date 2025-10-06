
from scanner.port_scanner import run_port_scan
from scanner.vuln_scanner import run_vuln_scan
from scanner.firewall_check import check_firewall
from auth.password_policy import check_password_strength
from reports.report_writer import save_report
from reports.pdf_generator import generate_pdf 
from db.database import save_scan, init_db
from utils.logger import log_info, log_warning, log_error 

def run_audit(ip):
    log_info(f"STARTING FULL AUDIT on target IP: {ip}")
    print(f"\n[🔎] Running full audit on {ip} ...")
    init_db()

    log_info(f"Initiating port scan on {ip}")
    print(f"\n[🔎] Running port scan on {ip} ...")
    open_ports = run_port_scan(ip)
    
    log_info(f"Port scan complete. Open ports: {open_ports}")
    print(f"[✔] Open ports on {ip}: {open_ports}")

    log_info(f"Checking vulnerabilities for {ip}")
    print(f"\n[🔎] Checking vulnerabilities for {ip} ...")
    vulnerabilities = run_vuln_scan(ip)
    
    if vulnerabilities:
        log_warning(f"VULNERABILITY FINDINGS: {len(vulnerabilities)} issues found on {ip}.")
        print("[⚠️] Vulnerabilities found:")
        for v in vulnerabilities:
            print(" -", v)
    else:
        log_info(f"Vulnerability check clean on {ip}.")
        print("[✔] No major vulnerabilities found.")

    log_info(f"Checking firewall rules for {ip}")
    print(f"\n[🔎] Checking firewall for {ip} ...")
    firewall_issues = check_firewall(open_ports)
    
    if firewall_issues:
        log_warning(f"FIREWALL FINDINGS: {len(firewall_issues)} issues detected on {ip}.")
        print("[⚠️] Firewall issues detected:")
        for f in firewall_issues:
            print(" -", f)
    else:
        log_info(f"Firewall check clean on {ip}.")
        print("[✔] Firewall looks fine.")

    log_info("Starting password policy audit.")
    password = input("\nEnter a password to audit: ")
    password_issues = check_password_strength(password)
    
    if password_issues:
        log_warning("PASSWORD POLICY FINDINGS: Weak password detected.")
        print("[⚠️] Password issues:")
        for p in password_issues:
            print(" -", p)
    else:
        log_info("Password strength check passed.")
        print("✅ Strong password!")

    
    report_file_txt = save_report(ip, open_ports, vulnerabilities, firewall_issues, password_issues, report_type="txt")
    log_info(f"Text report successfully saved to: {report_file_txt}")
    print(f"\n📄 Text Report saved to: {report_file_txt}")

    report_file_pdf = generate_pdf(ip, open_ports, vulnerabilities, firewall_issues, password_issues)
    if report_file_pdf:
        log_info(f"PDF report successfully created: {report_file_pdf}")
        print(f"📄 PDF Report saved to: {report_file_pdf}")
    else:
        log_error(f"Failed to generate PDF report for {ip}.")

    save_scan(ip, open_ports, vulnerabilities, firewall_issues, password_issues)
    log_info(f"Scan results successfully logged to database for {ip}.")
    print("💾 Scan results saved to database.")
    log_info(f"FULL AUDIT COMPLETE for {ip}")