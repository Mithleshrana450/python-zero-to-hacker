import re
from datetime import datetime

# Input
choice = input("1. Manual Input\n2. File Input\nEnter choice: ")

if choice == "1":
    text = input("Enter text: ")
else:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        text = file.read()

# Extract data
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', text)
urls = re.findall(r'https?://\S+|www\.\S+', text)
phones = re.findall(r'\b\d{10}\b', text)
md5 = re.findall(r'\b[a-fA-F0-9]{32}\b', text)
sha256 = re.findall(r'\b[a-fA-F0-9]{64}\b', text)

# Save report
with open("osint_report.txt", "w") as report:
    report.write("OSINT REPORT\n\n")
    report.write(f"Emails ({len(emails)}): {emails}\n")
    report.write(f"IPs ({len(ips)}): {ips}\n")
    report.write(f"URLs ({len(urls)}): {urls}\n")
    report.write(f"Phone Numbers ({len(phones)}): {phones}\n")
    report.write(f"MD5 Hashes ({len(md5)}): {md5}\n")
    report.write(f"SHA256 Hashes ({len(sha256)}): {sha256}\n")

# Log activity
with open("activity_log.txt", "a") as log:
    log.write(f"Program executed at: {datetime.now()}\n")

# Display counts
print("\nExtraction Completed!")
print("Emails:", len(emails))
print("IPs:", len(ips))
print("URLs:", len(urls))
print("Phone Numbers:", len(phones))
print("MD5 Hashes:", len(md5))
print("SHA256 Hashes:", len(sha256))

print("\nReport saved as osint_report.txt")
print("Log saved as activity_log.txt")