# URL analyzer:
# Take a URL as input: "https://target.com/admin/login.php?user=admin"
# Extract and print:

# Protocol (https)
# Domain (target.com)
# Path (/admin/login.php)
# Query string (user=admin)

url = "https://target.com/admin/login.php?user=admin"

# Split by "://"
protocol, rest   = url.split("://")           # https | target.com/admin/...

# Split by "/"
parts            = rest.split("/")
domain           = parts[0]                   # target.com

# Split path and query
path_and_query   = "/" + "/".join(parts[1:])  # /admin/login.php?user=admin
if "?" in path_and_query:
    path, query  = path_and_query.split("?")
else:
    path, query  = path_and_query, "None"

print("Protocol    :", protocol)
print("Domain      :", domain)
print("Path        :", path)
print("Query string:", query)
