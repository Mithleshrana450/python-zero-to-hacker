class HackingTool:
    tool_count = 0

    def __init__(self, name, version, author):
        self.name = name
        self.version = version
        self.author = author
        self.results = []
        HackingTool.tool_count += 1

    def run(self):
        pass

    def save_results(self, filename):
        with open(filename, "w") as f:
            for r in self.results:
                f.write(r + "\n")

    def show_banner(self):
        print(f"{self.name} v{self.version} by {self.author}")

    def __str__(self):
        return f"{self.name} v{self.version}"


class PortScanner(HackingTool):
    def __init__(self, name, version, author, target, ports):
        super().__init__(name, version, author)
        self.target = target
        self.ports = ports

    def run(self):
        for p in self.ports:
            self.results.append(f"Port {p} is Open")
        print("Port Scan Completed")


class BruteForcer(HackingTool):
    def __init__(self, name, version, author, target, wordlist):
        super().__init__(name, version, author)
        self.target = target
        self.wordlist = wordlist

    def run(self):
        self.results.append(f"Password found using {self.wordlist}")
        print("Brute Force Completed")


class OSINTTool(HackingTool):
    def __init__(self, name, version, author, target):
        super().__init__(name, version, author)
        self.target = target

    def run(self):
        self.results.append(f"Information collected for {self.target}")
        print("OSINT Completed")


# Example
p = PortScanner("Nmap", "1.0", "Mithlesh", "192.168.1.1", [22, 80, 443])
b = BruteForcer("Hydra", "2.0", "Mithlesh", "Login", "rockyou.txt")
o = OSINTTool("Recon", "1.0", "Mithlesh", "example.com")

for tool in [p, b, o]:
    tool.show_banner()
    tool.run()
    print(tool.results)
    print()

print("Total Tools:", HackingTool.tool_count)