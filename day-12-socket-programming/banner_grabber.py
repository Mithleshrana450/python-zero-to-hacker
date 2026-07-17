import socket

def grab_banner(host, port):
    s = socket.socket()
    s.settimeout(2)

    try:
        s.connect((host, port))

        # Send GET request only for HTTP
        if port == 80:
            s.send(b"GET / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n")

        banner = s.recv(1024)
        print("Banner from port", port)
        print(banner.decode(errors="ignore"))

    except:
        print("Could not get banner from port", port)

    s.close()


host = "scanme.nmap.org"

# Test SSH
grab_banner(host, 22)

print("-" * 40)

# Test HTTP
grab_banner(host, 80)