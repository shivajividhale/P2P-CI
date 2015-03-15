import socket

class connection:
    def __init__(self,p,a):
        self.server_port = port
        self.client_port = addr.port
        sock = self.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.bind(('localhost',self.server_port))
        sock.listen(1)
        while True:
            print("Hi")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',7734))
s.listen(5)
port = 9000
while True:

    (conn, addr) = s.accept()
    print(addr.port)
    conn.send(bytes(port, "UTF-8"))
    port = port +1
    k = connection(port,addr)

    rfc_list = conn.recv(100)
    print(rfc_list.decode("UTF-8"))
