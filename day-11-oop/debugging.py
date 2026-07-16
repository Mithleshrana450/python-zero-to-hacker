class Scanner:
    def __init__(self, ip):
        self.ip = ip

    def scan(self):
        print(f"Scanning {self.ip}")

class AdvancedScanner(Scanner):
    def __init__(self, ip, port):
        super().__init__(ip)
        self.port = port

    def scan(self):
        super().scan()
        print(f"Port: {self.port}")

s = AdvancedScanner("192.168.1.1", 80)
s.scan()

class Tool:
    count = 0
    def __init__(self):
        Tool.count += 1

t1 = Tool()
t2 = Tool()
print(Tool.count)