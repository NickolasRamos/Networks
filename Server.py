''''#server side

#the server verifies has an ID on the list of subscribers'''

from socket import *
from Functions import *



serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
    connectionSocket,addr=serverSocket.accept()
    user_Request = connectionSocket.recv(1024)
    validation = validate(int(user_Request))
    if validation == True:
        connectionSocket.send("Connected")
        print user_Request + " connected to the server"
    else:
        connectionSocket.send("User id not valid\n")




