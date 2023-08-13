import socket

def to_ip_address(domain_name):
    return socket.gethostbyname(domain_name)