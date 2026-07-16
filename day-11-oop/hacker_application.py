import hashlib
from datetime import datetime

class Vulnerability:
    """Represents a found vulnerability"""
    def __init__(self, cve, severity, description):
        self.cve         = cve
        self.severity    = severity
        self.description = description
        self.found_at    = datetime.now()

    def __str__(self):
        return f"[{self.severity}] {self.cve}: {self.description}"

class Target:
    """Represents a scan target"""
    def __init__(self, ip, hostname="Unknown"):
        self.ip            = ip
        self.hostname      = hostname
        self.open_ports    = []
        self.services      = {}
        self.vulns         = []
        self.scanned_at    = None

    def add_port(self, port, service):
        self.open_ports.append(port)
        self.services[port] = service

    def add_vuln(self, vuln):
        self.vulns.append(vuln)

    def get_risk_level(self):
        critical = sum(1 for v in self.vulns if v.severity == "CRITICAL")
        if critical > 0: return "CRITICAL"
        if len(self.vulns) > 3: return "HIGH"
        if len(self.open_ports) > 5: return "MEDIUM"
        return "LOW"

    def generate_report(self):
        print(f"\n{'='*50}")
        print(f"TARGET REPORT: {self.ip}")
        print(f"{'='*50}")
        print(f"Hostname  : {self.hostname}")
        print(f"Risk Level: {self.get_risk_level()}")
        print(f"Open Ports: {self.open_ports}")
        print(f"Vulns Found: {len(self.vulns)}")
        for v in self.vulns:
            print(f"  {v}")

# Usage
target = Target("192.168.1.1", "webserver.local")
target.add_port(22,  "SSH")
target.add_port(80,  "HTTP")
target.add_port(443, "HTTPS")
target.add_vuln(Vulnerability("CVE-2021-44228", "CRITICAL", "Log4Shell RCE"))
target.add_vuln(Vulnerability("CVE-2022-0847",  "HIGH",     "Dirty Pipe"))
target.generate_report()