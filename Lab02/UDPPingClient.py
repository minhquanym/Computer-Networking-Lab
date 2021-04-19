from socket import *
from datetime import datetime

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)    

num_loss = 0
RTTs = []

for sequence_number in range(1, 11):
    message = "Ping " + str(sequence_number) + " " + str(datetime.now())
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        values = modifiedMessage.decode().split()
        print("Modified Message: ", modifiedMessage)
    
        sendTime = datetime.strptime(str(values[2] + " " + values[3]), '%Y-%m-%d %H:%M:%S.%f')
        RTT = datetime.now() - sendTime
        print("RTT: ", RTT)

        RTTs.append(RTT)
    except:
        num_loss += 1
        print("Request timed out")


print("")
print("Min RTT: ", min(RTTs))
print("Max RTT: ", max(RTTs))
print("Average RTT", (sum([RTT.total_seconds() for RTT in RTTs]) / (10 - num_loss)))
print("Packet Loss Rate: ", float(num_loss / 10 * 100), "%")
clientSocket.close()
    