import socket
from binascii import hexlify

def convert_ip4_address():
    for ip_addr in ['127.0.0.1', '192.168.0.1']:
        # convert IPV4 format to 32-bit packed binary format
        packed_ip_addr = socket.inet_aton(ip_addr)
        # Convert a 32-bit packed IPv4 address (a bytes-like object four bytes in length) to its standard dotted-quad string representation
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print(f"IP Address: {ip_addr} => Packed: {hexlify(packed_ip_addr)}, Unpacked: {unpacked_ip_addr}")


if __name__ == "__main__":
    convert_ip4_address()