from scapy.all import sniff, IP, TCP, UDP, wrpcap
import os

def start_sniffer(count=10, timeout=10):
    """
    Captures a specified number of packets or runs for a given timeout.
    
    Args:
        count (int): Number of packets to capture.
        timeout (int): Time limit in seconds for sniffing.
    
    Returns:
        list: A list of captured packets.
    """
    print(f"\n[📡] Starting packet capture (Sniffing {count} packets or for {timeout}s)...")
    packets = sniff(count=count, timeout=timeout, filter='ip', store=True)

    if packets:
        print(f"[✔] Captured {len(packets)} packets.")
    else:
        print("[⚠️] No packets captured. Check network connectivity or permissions.")

    return packets

def save_packets(packets, filename="captured_traffic.pcap"):
    """Saves captured packets to a .pcap file."""
    pcap_path = os.path.join("reports", filename)
    
    try:
        wrpcap(pcap_path, packets)
        print(f"[✔] Captured packets saved to {pcap_path}")
    except Exception as e:
        print(f"[❌] Error saving pcap file: {e}")
    
    return pcap_path

if __name__ == "__main__":
    captured_packets = start_sniffer(count=5)
    if captured_packets:
        save_packets(captured_packets)
        
    
        print("\n--- Summary of First 2 Packets ---")
        for i, pkt in enumerate(captured_packets[:2]):
            print(f"Packet {i+1}: {pkt.summary()}")