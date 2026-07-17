import socket

hosts = [
    "google.com",
    "scanme.nmap.org",
    "github.com",
    "python.org"
]

print("-" * 50)
print("Hostname\t\tIP Address\t\tPort 80")
print("-" * 50)

for host in hosts:
    try:
        ip = socket.gethostbyname(host)

        s = socket.socket()
        s.settimeout(2)

        if s.connect_ex((ip, 80)) == 0:
            status = "Open"
        else:
            status = "Closed"

        s.close()

        print(host, "\t", ip, "\t", status)

    except:
        print(host, "\t Error")