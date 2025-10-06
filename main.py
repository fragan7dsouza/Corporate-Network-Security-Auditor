# main.py

import sys
from utils.logger import configure_logging 
from db.database import init_db, get_scans
from scanner.port_scanner import run_port_scan
from scanner.vuln_scanner import run_vuln_scan
from auditor import run_audit
from network.packet_sniffer import start_sniffer
from network.traffic_analyzer import analyze_packets


def view_scans():
    """Fetches the most recent scans from the database and displays them."""
    init_db() 
    scans = get_scans(limit=10) 

    if not scans:
        print("\n\u274c No scans found in the database. Run Option 3 (Full Audit) first!")
        return

    print("\n[📊] Showing last {} audits:".format(len(scans))) 
    for scan in scans:
        print("--------------------------------------------------")
        print(f"ID: {scan[0]}, IP: {scan[1]}, Time: {scan[2]}")
        print(f"  Ports: {scan[3]}")
        print(f"  Vulnerabilities: {scan[4].replace('\\n', ' | ')}") 
        print(f"  Firewall Issues: {scan[5].replace('\\n', ' | ')}")
        print(f"  Password Issues: {scan[6].replace('\\n', ' | ')}")
        print("--------------------------------------------------")


def run_network_audit():
    """Sniffs traffic and analyzes it for anomalies and unencrypted data."""
    packets = start_sniffer(count=15, timeout=10) 
    
    if not packets:
        return

    findings = analyze_packets(packets)
    
    print("\n--- Network Audit Summary ---")
    if findings:
        print(f"[❌] {len(findings)} Security Issues Detected:")
        for issue in findings:
            print(f" - {issue}")
    else:
        print("[✅] No immediate security issues or cleartext traffic detected.")
        
    print("\n[i] The raw traffic (.pcap) file has been saved to the reports directory for manual inspection.")


def main_menu():
    configure_logging() 
    init_db()
    
    while True:
        print("\nCorporate Network Security Auditor")
        print("----------------------------------")
        print("1. Run Port Scan")
        print("2. Run Vulnerability Scan")
        print("3. Run Full Audit (Static)")
        print("4. View Scan History")
        print("5. Run Network Traffic Audit")
        print("6. Exit")

        choice = input("\n\nEnter your choice (1-6): ").strip()

        if choice == "1":
            ip = input("Enter target IP: ").strip()
            run_port_scan(ip)
        elif choice == "2":
            ip = input("Enter target IP: ").strip()
            open_ports = run_port_scan(ip)
            run_vuln_scan(ip, open_ports)
        elif choice == "3":
            ip = input("Enter target IP: ").strip()
            run_audit(ip)
        elif choice == "4":
            view_scans()
        elif choice == "5":
            run_network_audit()
        elif choice == "6":
            print("Exiting... stay secure! 🔒")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main_menu()