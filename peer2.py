__author__ = 'Shivaji'
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
s.connect(('localhost', 7734))
ack = s.recv(100)
if ack == False:
    print("Received nothing")
else:
    print("Recieved something")
    print(str(ack))
ack = ack.decode("UTF-8")
print("Printing ACK:")
print(ack)
sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sd.connect(('localhost', int(ack)))
print(sd)
rfc_list = "123 496 612"
sd.send(bytes(rfc_list,'UTF-8'))
sd.send(bytes("2nd transfer",'UTF-8'))
print("Sent 2nd trnasfer")

