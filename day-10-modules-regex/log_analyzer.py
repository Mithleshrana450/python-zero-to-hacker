import re

pythonlogs = [
    "2026-07-09 14:32:11 FAILED LOGIN admin 192.168.1.105",
    "2026-07-09 14:32:15 FAILED LOGIN admin 192.168.1.105",
    "2026-07-09 14:32:19 FAILED LOGIN root  192.168.1.105",
    "2026-07-09 14:33:01 SUCCESS LOGIN admin 10.0.0.1",
    "2026-07-09 14:33:11 FAILED LOGIN admin 192.168.1.200",
    "2026-07-09 14:33:15 FAILED LOGIN root  192.168.1.105",
    "2026-07-09 14:33:19 FAILED LOGIN admin 192.168.1.105",
]

failed = []
count = {}

for log in pythonlogs:
    if re.search(r"FAILED LOGIN", log):
        failed.append(log)

        ip = re.search(r"\d+\.\d+\.\d+\.\d+", log).group()

        if ip in count:
            count[ip] += 1
        else:
            count[ip] = 1

print("Failed Login Attempts:")
for i in failed:
    print(i)

print("\nUnique Failed IPs:")
for ip in count:
    print(ip)

print("\nFailures Per IP:")
for ip in count:
    print(ip, ":", count[ip])

print("\nIPs with More Than 3 Failures:")
for ip in count:
    if count[ip] > 3:
        print(ip)