with open("targets.txt") as f:
    content = f.read()

try:
    port = int(input("Enter port: "))
    result = 100 / port
except:
    print("Error")
finally:
    print("Done")

f = open("log.txt", "w")
f.write("Scan complete")
f.close()

import os
if os.path.exists("file.txt"):
    print("File found")