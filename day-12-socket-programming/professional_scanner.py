import socket
import time
from datetime import datetime

# Start time
start_time = time.time()

# Target
target = input("Enter IP address or Hostname: ")

try:
    ip = socket.gethostbyname(target)
except:
    print("Invalid Hostname or IP")
    exit()

# Port range
choice = input("Scan default ports (1-1024)? (y/n): ")

if choice.lower() == "y":
    start_port = 1
    end_port = 1024
else:
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

print("\nScanning:", target, "(", ip, ")")
print("Started at:", datetime.now())
print("-" * 60)

# Report file
report = open("port_scan_report.txt", "w")
report.write("Port Scanner Report\n")
report.write("Target: " + target + " (" + ip + ")\n")
report.write("-" * 60 + "\n")

open_ports = 0

for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        result = s.connect_ex((ip, port))

        if result == 0:
            open_ports += 1

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            # Banner Grabbing
            banner = ""
            try:
                if port == 80:
                    s.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                banner = s.recv(1024).decode(errors="ignore").strip()
            except:
                banner = "No Banner"

            print("Port:", port)
            print("Service:", service)
            print("Banner:", banner)
            print("-" * 60)

            report.write(f"Port: {port}\n")
            report.write(f"Service: {service}\n")
            report.write(f"Banner: {banner}\n")
            report.write("-" * 60 + "\n")

    except:
        pass

    s.close()

report.write(f"\nTotal Open Ports: {open_ports}\n")
report.close()

end_time = time.time()

print("\nScan Completed")
print("Total Open Ports:", open_ports)
print("Time Taken: %.2f seconds" % (end_time - start_time))
print("Report saved as 'port_scan_report.txt'")