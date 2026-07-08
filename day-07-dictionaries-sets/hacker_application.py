# Real vulnerability scanner data structure
scan_results = {
    "192.168.1.1": {
        "open_ports" : [22, 80, 443],
        "services"   : {22: "SSH", 80: "HTTP", 443: "HTTPS"},
        "os"         : "Ubuntu 20.04",
        "risk"       : "Medium",
        "vulns"      : ["CVE-2021-44228", "CVE-2022-0847"]
    },
    "192.168.1.2": {
        "open_ports" : [23, 3306],
        "services"   : {23: "Telnet", 3306: "MySQL"},
        "os"         : "Windows Server 2019",
        "risk"       : "Critical",
        "vulns"      : ["Telnet unencrypted", "MySQL exposed"]
    }
}

def generate_report(results):
    print("=" * 55)
    print("         VULNERABILITY SCAN REPORT")
    print("=" * 55)
    for ip, data in results.items():
        print(f"\n[HOST] {ip}")
        print(f"  OS       : {data['os']}")
        print(f"  Risk     : {data['risk']}")
        print(f"  Ports    : {data['open_ports']}")
        print(f"  Vulns    : {len(data['vulns'])} found")
        for v in data['vulns']:
            print(f"    → {v}")

generate_report(scan_results)