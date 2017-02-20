from socket import socket, SOCK_STREAM, AF_INET

HOST = '192.168.1.8'    
PORT = 5555             
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    s.sendall(input("Inserire dato da inviare: "))
    data = s.recv(1024)
    print 'Received', repr(data)
s.close()

