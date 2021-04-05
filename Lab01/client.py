from socket import *
import sys

serverName = sys.argv[1]
serverPort = int(sys.argv[2])
clientServer = socket(AF_INET, SOCK_STREAM)
clientServer.connect((serverName, serverPort))

filename = sys.argv[3]
clientServer.sendall(("GET /" + filename + " HTTP/1.1\r\n\r\n").encode())

message = clientServer.recv(1024).decode()
print(message)
clientServer.close()
