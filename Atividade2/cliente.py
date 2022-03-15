import socket
import struct
import sys

# Cria um socket UDP e o configura
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)                                                  # Timeout in seconds
ttl = struct.pack('b', 1)                                           # Set TTL to 1 hop (limits the network reach to local-only)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)    # Define socket options

expression_string = bytes(input("Entre com a expressão:"), "utf-8")

try:
    sent = sock.sendto(expression_string, ("224.14.0.244", 64031))
    while True:
        try:
            recv_message, server_address = sock.recvfrom(64)
        except socket.timeout:
            break
        else:
            print(f"{recv_message}")
finally:
    sock.close()