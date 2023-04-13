from socket import *
import sys


name_of_server = input("Enter IP address of the server: ") # replace this with the IP address of the server PC
port_of_server = int(input("Enter port number of the server: ")) # replace this with the port number of the server PC
client_integer = int(input('Enter an integer from 1 to 100:'))
name_of_client = "client of Hussein Mohammed"

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((name_of_server, port_of_server))

message = f"{name_of_client} {client_integer}"
clientSocket.send(message.encode())

server_message = clientSocket.recv(5000).decode()
if not server_message:
    print("server is shutting down")
    clientSocket.close()
    sys.exit()

list_of_word = server_message.split()
server_number = int(list_of_word[-1])

print('From Server:', *list_of_word[:-1])
print("client:", name_of_client)
print(f"client_integer: {client_integer}")
print(f"server_number: {server_number}")
print("sum:",server_number+client_integer)

clientSocket.close()