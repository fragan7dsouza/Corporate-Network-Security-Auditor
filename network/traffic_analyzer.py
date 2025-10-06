
from scapy.all import IP, TCP, UDP
from collections import defaultdict

def analyze_packets(packets):
    """
    Analyzes a list of captured packets for basic security risks and patterns.
    
    Args:
        packets (list): A list of packets captured by the sniffer.
        
    Returns:
        list: A list of security issues detected.
    """
    issues = []
    unencrypted_ports = {
        21: "FTP (File Transfer Protocol)",
        23: "Telnet (Remote Login)",
        80: "HTTP (Web traffic)",
        110: "POP3 (Email retrieval)",
        143: "IMAP (Email access)"
    }
    
    for pkt in packets:
        if TCP in pkt:
            dst_port = pkt[TCP].dport
            if dst_port in unencrypted_ports:
                issue = (
                    f"⚠️ Cleartext Traffic Detected: Packet from {pkt[IP].src} to {pkt[IP].dst} "
                    f"is using {unencrypted_ports[dst_port]} (Port {dst_port}). Data is unencrypted."
                )
                if issue not in issues:
                    issues.append(issue)
    ip_port_count = defaultdict(set)
    for pkt in packets:
        if IP in pkt and TCP in pkt:
            ip_port_count[pkt[IP].src].add(pkt[TCP].dport)

    for src_ip, ports in ip_port_count.items():
        if len(ports) > 10 and len(packets) > 20: 
            issues.append(f"🔍 Potential Port Scan: Source IP {src_ip} contacted {len(ports)} unique ports in a short time.")


    return issues


if __name__ == "__main__":
    from packet_sniffer import start_sniffer 
    print("\n--- Running Integrated Traffic Analysis Test ---")

    captured_packets = start_sniffer(count=15, timeout=10)
    
    if captured_packets:
        security_findings = analyze_packets(captured_packets)
        
        print("\n--- Security Analysis Results ---")
        if security_findings:
            print(f"[❌] {len(security_findings)} Issues Detected:")
            for issue in security_findings:
                print(f" - {issue}")
        else:
            print("[✅] No major unencrypted traffic or anomalies detected in the sample.")