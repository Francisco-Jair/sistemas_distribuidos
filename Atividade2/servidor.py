import socket
import struct
import sys
import threading
import time


def multicast_ping():
    """Pegar o proprio ID na rede multicast"""
    ping_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ping_socket.settimeout(0.5)
    socketTTL = struct.pack('b', 1)
    ping_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, socketTTL) #Definir a opção do socket
    enderecos_multicast = ("224.14.0.244", 1902)
    bytes_sent = ping_socket.sendto(b'PING', enderecos_multicast)
    
    server_id = 1
    cont_msg = 0
    resposta = []

    while True:
        try:
            msg_recebida, endereco_remetente = ping_socket.recvfrom(64)
            if msg_recebida:
                cont_msg += 1
                receive_id = int(msg_recebida.decode("utf-8"))
                resposta.append(receive_id)
                server_id = max(server_id, receive_id + 1)
        except socket.timeout:
            break

    ping_socket.close()
    return server_id, resposta


def multicast_ping_respond(server_id):
    endereco_local = ("", 1902)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(endereco_local)
    group = socket.inet_aton("224.14.0.244")
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        recv_message, client_address = sock.recvfrom(64)
        msg = recv_message.decode("utf-8")
        if msg == "PING":
            id_bytestr = str(server_id).encode("utf-8")
            sent = sock.sendto(id_bytestr, client_address)

    sock.close()


def multicast_should_respond_expression(server_id):
    _ , responded = multicast_ping()
    responded.sort()
    if server_id in responded:
        if responded.index(server_id) == 0:
            return True
    return False


def resolver_expressao(expression_string):
    try:
        return eval(expression_string)
    except:
        return None


if __name__ == "__main__":
    # 1. Pegar o proprio ID na rede multicast
    server_id, responded = multicast_ping()

    # 2. Criar threading para responder a msg de ping
    ping_responding_thread = threading.Thread(target=multicast_ping_respond, args=[server_id])
    ping_responding_thread.start()

    # 3. Criar um socket UDP para responder os calculos
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 64031))
    group = socket.inet_aton("224.14.0.244")
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        recv_message, client_address = sock.recvfrom(64)
        should_respond = multicast_should_respond_expression(server_id)
        if should_respond:
            expression = recv_message.decode("utf-8")
            resolucao = resolver_expressao(expression)
            sock.sendto(str(resolucao).encode("utf-8"), client_address)
        else:
            pass
    
    ping_responding_thread.stop()
    