import nmap
from config.config_loader import SETTINGS

def run_port_scan(ip):
    port_range = SETTINGS.get("scan_settings", {}).get("port_range", "1-1024")
    
    print(f"\n[🔎] Running port scan on {ip} (Range: {port_range}) ...")
    scanner = nmap.PortScanner()
    
    scanner.scan(ip, port_range) 

    open_ports = []
    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            open_ports.extend([int(p) for p in ports]) 

    print(f"[✔] Open ports on {ip}: {open_ports}")
    return open_ports
