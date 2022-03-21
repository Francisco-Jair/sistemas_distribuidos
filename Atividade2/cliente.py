import socket
import struct
import sys

# Cria um socket UDP e o configura
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(2)                                                 
ttl = struct.pack('b', 1)                                          
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)    

expressao_em_string = bytes(input("Entre com a expressão:"), "utf-8")

try:
    sent = sock.sendto(expressao_em_string, ("224.14.0.244", 64031))
    while True:
        try:
            mensagem_recebida, endereco_servidor = sock.recvfrom(64)
        except socket.timeout:
            break
        else:
            print(mensagem_recebida)
finally:
    sock.close()