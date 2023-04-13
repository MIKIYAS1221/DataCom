from socket import *
import sys
import random

name_of_server_owner = "server of Mikiyas Mohammed"
port = 9876
socket_wifi = socket(AF_INET, SOCK_DGRAM)
socket_wifi.connect(("8.8.8.8", 80))
ip_address = socket_wifi.getsockname()[0]
socket_wifi.close()

print("Welcome to Mikiyas Mohammed's server")
print("If you want to connect to this server, use the following information:")
print(f"IP address: {ip_address}")
print(f"port: {port}")

try:
    server_socket = socket(AF_INET, SOCK_STREAM)
except:
    print("Socket creation failed")
    sys.exit()

server_socket.bind(('', port))
server_socket.listen(1)
print("The server is ready to receive")

while True:
    connection_socket, address = server_socket.accept()
    print("connection from", address)
    sentence = connection_socket.recv(2500).decode()
    list_of_words = sentence.split()

    name_of_client = list_of_words[:4]
    client_integer = int(list_of_words[-1])
    
    print("client:", *name_of_client)
    print(f"server: {name_of_server_owner}")

    if 0 <= client_integer <= 100:

        server_number = random.randint(0, 100)
        print(f"client_integer: {client_integer}")
        print(f"server_number: {server_number}")
        print("sum:", client_integer + server_number)

        connection_socket.send(f"{name_of_server_owner} {server_number}".encode())
        connection_socket.close()

    else:

        print("client_integer is out of range")
        connection_socket.close()
        server_socket.close()
        sys.exit()
        
    





    