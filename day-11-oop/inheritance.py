class SecurityTool:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def run(self):
        print("Running security tool...")

    def __str__(self):
        return f"{self.name} v{self.version}"


class PortScanner(SecurityTool):
    def __init__(self, name, version, target):
        super().__init__(name, version)
        self.target = target

    def run(self):
        print(f"Scanning ports on {self.target}")

    def __str__(self):
        return f"PortScanner: {self.name} v{self.version}, Target: {self.target}"


class WebScanner(SecurityTool):
    def __init__(self, name, version, target):
        super().__init__(name, version)
        self.target = target

    def run(self):
        print(f"Scanning website {self.target}")

    def __str__(self):
        return f"WebScanner: {self.name} v{self.version}, Target: {self.target}"


class PasswordCracker(SecurityTool):
    def __init__(self, name, version, wordlist):
        super().__init__(name, version)
        self.wordlist = wordlist

    def run(self):
        print(f"Cracking passwords using {self.wordlist}")

    def __str__(self):
        return f"PasswordCracker: {self.name} v{self.version}, Wordlist: {self.wordlist}"


# Example
p = PortScanner("Nmap", "1.0", "192.168.1.1")
w = WebScanner("Nikto", "2.1", "example.com")
c = PasswordCracker("John", "3.0", "rockyou.txt")

print(p)
p.run()

print(w)
w.run()

print(c)
c.run()