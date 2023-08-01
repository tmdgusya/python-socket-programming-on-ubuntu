import socket

def get_remote_machine_info():
    """
    Get IP address of remote host from socket
    """
    remote_host = 'www.naver12312.org'
    try:
        print(f"IP address of {remote_host}: {socket.gethostbyname(remote_host)}")
    except socket.error as err_msg:
        print(f"{remote_host}: {err_msg}")

if __name__ == "__main__":
    get_remote_machine_info()