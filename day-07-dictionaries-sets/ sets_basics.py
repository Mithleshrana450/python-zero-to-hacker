scan_tcp = {21, 22, 80, 443, 3306, 8080}
scan_udp = {53, 80, 443, 161, 162, 8080}

print("All unique ports:", scan_tcp | scan_udp)
print("Common ports:", scan_tcp & scan_udp)
print("Only TCP ports:", scan_tcp - scan_udp)
print("Only UDP ports:", scan_udp - scan_tcp)