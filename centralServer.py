import socket
import threading
def make_connection( port, addr):
    server_port = port
    client_address = addr
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(('localhost',server_port))
    sock.listen(1)
    while True:
        (client_socket, client_addr) = sock.accept()
        rfc_list = client_socket.recv(100)
        print("Hi: "+str(client_addr))
        print(rfc_list.decode("UTF-8"))
        #client_socket.listen(1)
        #while True:
        msg = client_socket.recv(100)
        print(msg.decode('UTF-8'))

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',7734))
s.listen(5)
port = 9000
while True:

    (conn, addr) = s.accept()
    print("Received a connection from:")
    print(addr)
    port = port +1
    conn.send(bytes(str(port), "UTF-8"))
    print("Sent:"+str(bytes(str(port), "UTF-8")))
    print("Sent port number:"+str(port))
    t = threading.Thread(name = addr, target = make_connection, args=( port, addr,))
    t.start()

    #rfc_list = conn.recv(100)
    #print(rfc_list.decode("UTF-8"))
