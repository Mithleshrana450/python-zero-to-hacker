# Real recon tool structure — every professional
# hacking script is built exactly like this

def get_target():
    target = input("Enter target IP: ")
    return target

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    open_ports = []
    for port in ports:
        # real scanner uses socket here
        # we simulate for now
        if port in [22, 80, 443]:
            open_ports.append(port)
    return open_ports

def generate_report(target, open_ports):
    print("=" * 40)
    print("SCAN REPORT")
    print("=" * 40)
    print("Target:", target)
    print("Open ports:", open_ports)
    print("Total found:", len(open_ports))
    print("=" * 40)

# Main execution
target = get_target()
ports = range(1, 1025)
results = scan_ports(target, ports)
generate_report(target, results)