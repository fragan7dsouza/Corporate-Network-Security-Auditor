def check_firewall(open_ports):
    risky_ports = {
        21: "FTP - cleartext authentication",
        23: "Telnet - insecure protocol",
        445: "SMB - ransomware target"
    }
    issues = []
    for port in open_ports:
        if port in risky_ports:
            issues.append(f"Port {port}: {risky_ports[port]} allowed by firewall")
    return issues

if __name__ == "__main__":
    #quick test
    test_ports = [21, 80, 445]
    findings = check_firewall(test_ports)
    print("🔒 Firewall Findings:")
    for f in findings:
        print(" -", f)
