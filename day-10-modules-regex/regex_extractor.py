import re

pythontext = """
Contact admin@company.com or support@target.org
Server at 192.168.1.1 and backup at 10.0.0.254
Visit https://target.com/admin or http://192.168.1.1:8080
Call +91-9876543210 for support
Hash: 5f4dcc3b5aa765d61d8327deb882cf99
"""

emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', pythontext)
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', pythontext)
urls = re.findall(r'https?://[^\s]+', pythontext)
phones = re.findall(r'\+91-\d{10}', pythontext)
md5 = re.findall(r'\b[a-fA-F0-9]{32}\b', pythontext)

print("Emails:", emails)
print("IPs:", ips)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("MD5 Hash:", md5)