from hacker_utils import *

md5, sha = hash_password("hello123")
print("MD5:", md5)
print("SHA256:", sha)

print(is_valid_ip("192.168.1.1"))

print(get_service(80))

print(generate_random_password(8))