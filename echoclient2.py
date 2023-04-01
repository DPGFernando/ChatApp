import socket
port = 1236
address = '127.0.0.1'
BUF_SIZE = 15
HEADER_SIZE = 10
# create a socket object name 'con'
con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
con.connect((address, port))

message =""
newmsg = True

while True:
    data = con.recv(BUF_SIZE)
    if newmsg:
        msg_length = int(data[:HEADER_SIZE].decode("utf-8"))
        #print(msg_length)
        message+=data[HEADER_SIZE:].decode("utf-8")
        newmsg = False
    else:
        message+=data.decode("utf-8")
        
    #print(len(full_msg))
    if(len(message)>=msg_length):
        #print("full message received")
        print(message)
        break


con.close()
