"""

Author: AIden R Nairne
email: anairn12@caledonin.ac.uk

"""


import socket


UDP_IP =input("What is the ip?")
UDP_PORT= input("What is the port number?")
MESSAGE=input("What is the message?")

print(UDP_IP,type(UDP_IP))
print(UDP_PORT,type(UDP_PORT))
print(MESSAGE,type(MESSAGE))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(), (UDP_IP,int(UDP_PORT)))
