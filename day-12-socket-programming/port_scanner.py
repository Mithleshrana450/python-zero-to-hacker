import socket

ip = input("Enter IP address: ")
start = int(input("Enter starting port: "))
end = int(input("Enter ending port: "))

open_ports = 0

print("\nScanning...\n")

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)  # Timeout of 1 second

    result = s.connect_ex((ip, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"

        print("Port", port, "-", service, ": Open")
        open_ports += 1

    s.close()

print("\nTotal Open Ports:", open_ports)