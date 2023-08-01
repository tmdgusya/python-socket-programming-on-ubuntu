import socket

def find_service_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print(f"Port: {port} => service name: {socket.getservbyport(port, protocolname)}")


if __name__ == "__main__":
    find_service_name()