import socket
import threading
import time
from datetime import datetime

class PortScanner:
    """Professional port scanner using OOP + sockets"""

    def __init__(self, target, start_port=1, end_port=1024, timeout=0.5):
        self.target     = target
        self.start_port = start_port
        self.end_port   = end_port
        self.timeout    = timeout
        self.open_ports = []
        self.lock       = threading.Lock()

    def resolve_target(self):
        try:
            return socket.gethostbyname(self.target)
        except socket.gaierror:
            print(f"[-] Cannot resolve {self.target}")
            return None

    def scan_port(self, ip, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                with self.lock:
                    self.open_ports.append((port, service))
            s.close()
        except:
            pass

    def run(self):
        ip = self.resolve_target()
        if not ip:
            return

        print(f"\n{'='*50}")
        print(f"  PORT SCANNER")
        print(f"{'='*50}")
        print(f"Target   : {self.target} ({ip})")
        print(f"Range    : {self.start_port}-{self.end_port}")
        print(f"Started  : {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'='*50}\n")

        start = time.time()
        threads = []
        for port in range(self.start_port, self.end_port + 1):
            t = threading.Thread(target=self.scan_port, args=(ip, port))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        elapsed = time.time() - start
        self.open_ports.sort()

        print("\n[RESULTS]")
        for port, service in self.open_ports:
            print(f"  {port:<6} OPEN   {service}")

        print(f"\n[*] {len(self.open_ports)} open ports found")
        print(f"[*] Scan completed in {elapsed:.2f} seconds")

# Run it
scanner = PortScanner("scanme.nmap.org", 1, 1024)
scanner.run()