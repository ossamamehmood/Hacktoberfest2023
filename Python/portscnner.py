import socket

def scan_ports(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

target = input("Enter the target IP address: ")
ports = range(1, 1001)  # Scanning ports from 1 to 1000
open_ports = scan_ports(target, ports)
print("Open ports:", open_ports)
