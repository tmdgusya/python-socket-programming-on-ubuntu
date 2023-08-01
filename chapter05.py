import socket

def convert_integer():
    data = 1234
    
    # ntohl function converts network byte order to host byte order in long type.
    # n => network
    # h => host
    print(f"Original: {data} => Long host byte order: {socket.ntohl(data)}, Network Byte order: {socket.htonl(data)}")
    print(f"Original: {data} => Short host byte order: {socket.ntohs(data)}, Network Byte order: {socket.htons(data)}")
    

if __name__ == "__main__":
    convert_integer()