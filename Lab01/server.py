#import socket module
from socket import *
import _thread
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 1234))
serverSocket.listen(5)

def on_new_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send(('HTTP/1.1 200 OK\r\n\r\n').encode())
        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\r".encode())

        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(('HTTP/1.1 404 Not Found\r\n\r\n').encode())
        # Close client socket
        connectionSocket.close()

while True:
    # Establish the connection
    print('Ready to server...')
    connectionSocket, addr = serverSocket.accept()
    _thread.start_new_thread(on_new_client, (connectionSocket, addr))

serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data
