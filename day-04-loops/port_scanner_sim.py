# Mini Project — Port Scanner Simulator
# # Simulate scanning ports 1 to 1024
# # Mark these ports as "open": 22, 80, 443, 3306, 8080
# # All others are "closed"
# # Print status of each port
# # At the end print total open ports found

open_ports = [22, 80, 443, 3306, 8080]
count = 0

print("Starting scan...")
for port in range(1, 1025):
    if port in open_ports:
        print("Port", port, "OPEN ✓")
        count += 1

print("Scan complete —", count, "open ports found")
