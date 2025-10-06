# view_scans.py

from db.database import get_scans

def view_recent_scans(limit=5):
    scans = get_scans(limit=limit)
    if not scans:
        print("❌ no scans found in database.")
        return

    print(f"\n📊 showing last {len(scans)} scans:")
    for scan in scans:
        print("\n----------------------------")
        print(f"scan id: {scan[0]}")
        print(f"ip: {scan[1]}")
        print(f"timestamp: {scan[2]}")
        print(f"open_ports: {scan[3]}")
        print(f"vulnerabilities: {scan[4]}")
        print(f"firewall_issues: {scan[5]}")
        print(f"password_issues: {scan[6]}")

if __name__ == "__main__":
    view_recent_scans(limit=5)
