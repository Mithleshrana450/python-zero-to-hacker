# Port scanner with list:
# Create a function scan(target, ports) that takes a target IP
# and a list of ports to scan. Print open/closed for each port.
# Open ports: [22, 80, 443]. Return list of open ports found.

open_ports = [22, 80, 443]

def scan(target, ports):
    print(f"\nScanning target: {target}")
    found_open = []

    for port in ports:
        if port in open_ports:
            print(f"Port {port} --> OPEN")
            found_open.append(port)
        else:
            print(f"Port {port} --> CLOSED")

    return found_open

# Test the function
result = scan("192.168.1.1", [22, 80, 443, 8080, 21])
print("\nOpen ports found:", result)