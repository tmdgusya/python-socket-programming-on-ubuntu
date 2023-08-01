import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Default Socket timeout: {s.gettimeout()}") # None
    s.settimeout(100)
    print(f"Current Socket timeout: {s.gettimeout()}")
    
    
if __name__ == "__main__":
    test_socket_timeout()