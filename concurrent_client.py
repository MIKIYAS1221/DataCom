from socket import *
import sys

def Main():
    server_host = "127.0.0.1"
    server_port = 9876

    # Replace "user1" and "password1" with the desired user and password from the server's user dictionary
    username = input("Enter username: ")
    password = input("Enter password: ")

    client_socket = socket(AF_INET, SOCK_STREAM)
    
    try:
        client_socket.connect((server_host, server_port))
    except:
        print("Connection to server failed")
        sys.exit()

    # Send credentials
    credentials = f"{username} {password}"
    client_socket.send(credentials.encode())

    # Receive and print the message of the day
    message_of_the_day = client_socket.recv(1024).decode('utf-8')
    print(message_of_the_day)

    # Existing client logic
    name_of_client_owner = "client of Mikiyas Mohammed"
    client_integer = int(input('Enter an integer from 1 to 100:'))
    client_sentence = f"{name_of_client_owner} {client_integer}"
    client_socket.send(client_sentence.encode())

    modified_sentence = client_socket.recv(1024).decode('utf-8')
    list_of_word = modified_sentence.split()
    server_number = int(list_of_word[-1])

    print('From Server:', *list_of_word[:-1])
    print("client:", name_of_client_owner)
    print(f"client_integer: {client_integer}")
    print(f"server_number: {server_number}")
    print("sum:",server_number+client_integer)
    print(modified_sentence)
    
    client_socket.close()

if __name__ == '__main__':
    Main()
