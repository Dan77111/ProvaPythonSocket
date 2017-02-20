from socket import socket, SOCK_STREAM, AF_INET



class Server():
    def __init__(self):
        sock = socket(AF_INET, SOCK_STREAM)
        global sock
        sock.bind(('',5555))
        sock.listen(1)
    def receive_data(self):
        conn, addr = sock.accept()
        print 'Connected by ', addr
        data = ""
        while data != 'STOP':
            data = conn.recv(1024)
            conn.sendall(data)
        conn.close()
server = Server()
server.receive_data()
