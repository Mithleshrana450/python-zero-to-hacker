targets = []

def add_target(ip, port, service):
    targets.append((ip, port, service))
    print(f"[+] Added: {ip}:{port} ({service})")

def remove_target(ip):
    for t in targets:
        if t[0] == ip:
            targets.remove(t)
            print(f"[-] Removed: {ip}")
            return
    print(f"[!] Target {ip} not found")

def show_targets():
    print("\n" + "="*45)
    print(f"{'IP':<18} {'PORT':<8} {'SERVICE'}")
    print("="*45)
    for ip, port, service in targets:
        print(f"{ip:<18} {port:<8} {service}")
    print("="*45)
    print(f"Total targets in scope: {len(targets)}")

# Test it
add_target("192.168.1.1", 80, "HTTP")
add_target("192.168.1.2", 22, "SSH")
add_target("192.168.1.3", 443, "HTTPS")
show_targets()
remove_target("192.168.1.2")
show_targets()