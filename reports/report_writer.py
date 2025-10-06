
import datetime
import os

def save_report(ip, open_ports, vulns=None, firewall_issues=None, password_issues=None, report_type="txt"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_name = f"scan_report_{ip}_{timestamp}.{report_type}"
    report_path = os.path.join("reports", report_name)

    vulns = vulns or []
    firewall_issues = firewall_issues or []
    password_issues = password_issues or []

    if report_type == "txt":
        with open(report_path, "w", encoding='utf-8') as f:
            f.write(f"Security Report for {ip}\n")
            f.write("=" * 50 + "\n\n")
            f.write("🔍 Open Ports:\n")
            if open_ports:
                f.writelines([f"- {p}\n" for p in map(str, open_ports)]) 
            else:
                f.write("None\n")
            f.write("\n")
            f.write("⚠️ Vulnerabilities:\n")
            if vulns:
                f.writelines([f"- {v}\n" for v in vulns])
            else:
                f.write("None\n")
            f.write("\n")
            f.write("🔒 Firewall Issues:\n")
            if firewall_issues:
                f.writelines([f"- {fw}\n" for fw in firewall_issues])
            else:
                f.write("None\n")
            f.write("\n")
            
            f.write("🔑 Password Policy Issues:\n")
            if password_issues:
                f.writelines([f"- {p}\n" for p in password_issues])
            else:
                f.write("None\n")
                
    print(f"\n[✔] Report saved to: {report_path}")
    return report_path