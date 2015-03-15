__author__ = 'Shivaji'
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.connect(('localhost', 7734))
ack = s.recv(100).decode("UTF-8")
print(ack)
print(s)
rfc_list = "123 456 632"
s.send(bytes(rfc_list,'UTF-8'))

