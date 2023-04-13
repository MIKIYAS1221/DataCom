from socket import *
import sys
from _thread import *
from random import randint

def Main():
    name_of_server_owner = "server of Mikiyas Mohammed"
    port = 9876
    message_of_the_day = "Welcome! The message of the day is: Enjoy the challenge!"

    users = {
        "Mikiyas": "12345678",
        "Minte": "87654321"
    }

    def verify_user(username, password):
        return username in users and users[username] == password

    def threaded(connection_socket):
        nonlocal name_of_server_owner

        try:
            # Verify user
            credentials = connection_socket.recv(1024).decode('utf-8').split()
            if len(credentials) != 2:
                connection_socket.send("Invalid credentials".encode())
                connection_socket.close()
                return

            username, password = credentials
            if not verify_user(username, password):
                connection_socket.send("Invalid credentials".encode())
                connection_socket.close()
                return

            # Send message of the day
            connection_socket.send(message_of_the_day.encode())

            while True:
                # Data received from client
                sentence = connection_socket.recv(2500)
                if not sentence:
                    print('Have a nice day!')
                    break

                # Process client input
                try:
                    list_of_words = sentence.decode('utf-8').split()
                    name_of_client = list_of_words[:4]
                    client_integer = int(list_of_words[-1])
                    print("client:", *name_of_client)
                    print(f"server: {name_of_server_owner}")
                except Exception as e:
                    print(f"Error processing client input: {e}")
                    break

                # Generate server response
                try:
                    if 0 <= client_integer <= 100:
                        server_number = randint(0, 100)
                        print(f"client_integer: {client_integer}")
                        print(f"server_number: {server_number}")
                        print("sum:", client_integer + server_number)
                        connection_socket.send(f"{name_of_server_owner} {server_number}".encode())
                        connection_socket.close()
                        break
                    else:
                        print("client_integer is out of range")
                        connection_socket.close()
                        break
                except Exception as e:
                    print(f"Error sending data to client: {e}")
                    break

        except Exception as e:
            print(f"Error receiving data from client: {e}")
        finally:
            # Connection closed
            connection_socket.close()

    try:
        server_socket = socket(AF_INET, SOCK_STREAM)
    except:
        print("Socket creation failed")
        sys.exit()

    server_socket.bind(('', port))
    server_socket.listen(2)
    print("The server is ready to receive")
    client_count = 0
    
    while True:

        connection_socket, address = server_socket.accept()
        print(f"Connected to : {address[0]} : {address[1]}")
        start_new_thread(threaded, (connection_socket,))
        client_count += 1

    server_socket.close()

if __name__ == '__main__':
    Main()
