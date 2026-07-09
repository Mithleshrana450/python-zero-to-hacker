log = "2026-07-01 14:32:11 FAILED LOGIN admin 192.168.1.105"

parts      = log.split()
date       = parts[0]    # 2026-07-01
time       = parts[1]    # 14:32:11
status     = parts[2]    # FAILED
action     = parts[3]    # LOGIN
username   = parts[4]    # admin
ip_address = parts[5]    # 192.168.1.105

print("Date      :", date)
print("Time      :", time)
print("Status    :", status)
print("Username  :", username)
print("IP Address:", ip_address)