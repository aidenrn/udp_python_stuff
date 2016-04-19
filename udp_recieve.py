"""

Author: Aiden R Nairne
Email: anairn12@caledonian.ac.uk

"""


import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main(ip,port):
	while True:


		sock.bind((ip,port))

		data, addr = sock.recvfrom(1024)
		print("recieved message:", data)


if __name__ == "__main__":
	
	main("127.0.0.1",9999)


