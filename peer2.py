__author__ = 'Shivaji'
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.connect(('localhost', 7734))
print(s)
rfc_list = "121 455 632"
s.send(bytes(rfc_list,'UTF-8'))
