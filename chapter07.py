import socket
import sys
import argparse


def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)
    
    given_args = parser.parse_args()
    
    host = given_args.host
    port = given_args.port
    filename = given_args.file
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1000)
    except socket.error as e:
        print(f"Error creating socket: {e}")
        sys.exit(1)
    
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f"Address-related error connecting to server: {e}")
        sys.exit(1)
    except socket.error as e:
        print(f"Connection error: {e}")
        sys.exit(1)
    
    try:
        s.sendall(bytes(f"GET {filename} HTTP/1.0\r\n\r\n", encoding='utf-8'))
    except socket.error as e:
        print(f"Error sending data: {e}")
        sys.exit(1)
    
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print(f"Error receiving data: {e}")
            sys.exit(1)
        if not len(buf):
            break
        
        sys.stdout.write(str(buf))

if __name__ == '__main__':
    main()
    

# poetry run python3 chapter07.py --host='www.pytgo.org' --port=8080 --file=1_7_socket_errors.py
# poetry run python3 chapter07.py --host='www.python.org' --port=8080 --file=1_7_socket_errors.py