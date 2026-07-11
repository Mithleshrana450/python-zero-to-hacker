import hashlib

known_hashes = [
    "5f4dcc3b5aa765d61d8327deb882cf99",   # password
    "e10adc3949ba59abbe56e057f20f883e"    # 123456
]

def check_password(password):
    md5 = hashlib.md5(password.encode()).hexdigest()
    sha1 = hashlib.sha1(password.encode()).hexdigest()
    sha256 = hashlib.sha256(password.encode()).hexdigest()

    if md5 in known_hashes:
        print("MD5 Hash Found!")
    else:
        print("MD5 Hash Not Found!")

    file = open("hashes.txt", "w")
    file.write("MD5: " + md5 + "\n")
    file.write("SHA1: " + sha1 + "\n")
    file.write("SHA256: " + sha256)
    file.close()

    print("Hashes saved to hashes.txt")

password = input("Enter Password: ")
check_password(password)