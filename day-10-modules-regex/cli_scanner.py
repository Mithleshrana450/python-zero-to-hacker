import sys

if len(sys.argv) < 3:
    print("Usage:")
    print("python scanner.py <IP> <PORT>")
    print("python scanner.py <IP> --range <START> <END>")
    exit()

ip = sys.argv[1]

if sys.argv[2] == "--range":
    start = int(sys.argv[3])
    end = int(sys.argv[4])

    print("Scanning", ip)
    for port in range(start, end + 1):
        print("Port", port, "is OPEN")

else:
    port = sys.argv[2]
    print("Scanning", ip)
    print("Port", port, "is OPEN")