import re
import hashlib
import sys

text = "Email: admin@test.com IP: 192.168.1.1"

# Extract email
emails = re.findall(r'[\w]+@[\w]+\.[\w]+', text)

# Extract IP
pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
ips = pattern.findall(text)

# Generate MD5 hash
hash_value = hashlib.md5("password".encode()).hexdigest()

# Check command-line argument
if len(sys.argv) > 1:
    target = sys.argv[1]
else:
    target = "No target provided"

# Print results
print("Emails:", emails)
print("IPs:", ips)
print("MD5:", hash_value)
print("Target:", target)