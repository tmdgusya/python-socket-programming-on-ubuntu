import socket

host_name = socket.gethostname()
id_address = socket.gethostbyname(host_name)

print(f"Host name: {host_name}")
print(f"Id Address: {id_address}")