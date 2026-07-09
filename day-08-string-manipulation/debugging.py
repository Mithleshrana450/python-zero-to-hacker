url = "https://target.com"

print(url.upper())

parts = url.split("://")
domain = parts[0]

password = "Hello123"
if password.isdigit():
    print("Has numbers")

words = "hello world"
print(words.replace("world" , "hacker"))

ip = "192.168.1.1"
print("IP is: " + ip)