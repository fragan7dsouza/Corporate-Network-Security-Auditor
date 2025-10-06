def run_vuln_scan(ip, open_ports=None):
    print(f"\n[🔎] Checking vulnerabilities for {ip} ...")

    vuln_db = {
        21: "FTP - Cleartext credentials, vulnerable to sniffing.",
        22: "SSH - Weak configurations may allow brute force.",
        23: "Telnet - Insecure, transmits data in plain text.",
        25: "SMTP - May be used for spam relay if misconfigured.",
        80: "HTTP - No encryption, vulnerable to MITM.",
        135: "MSRPC - Known for Windows exploits.",
        139: "NetBIOS - Can expose sensitive info.",
        445: "SMB - Common ransomware entry point.",
        3389: "RDP - Target for brute force and exploits."
    }

    findings = []
    if open_ports is None:
        open_ports = []  #safe default

    for port in open_ports:
        if port in vuln_db:
            findings.append(f"Port {port}: {vuln_db[port]}")

    if findings:
        print("[⚠️] Vulnerabilities found:")
        for f in findings:
            print(" -", f)
    else:
        print("[✔] No known vulnerabilities detected.")

    return findings
