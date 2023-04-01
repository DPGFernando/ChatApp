import socket
port = 1236
address = '127.0.0.1'
BUF_SIZE = 15
HEADER_SIZE = 10
# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

message = input("Enter your message :")

con.send(bytes("{msg_length:{hs}d}".format(msg_length=len(message),hs=HEADER_SIZE) + message,"utf-8"));

