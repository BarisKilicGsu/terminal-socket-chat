import socket
import threading

HOST_IP = "192.168.25.201"
HOST_PORT = 50007
ENCODER = "utf-8"
BYTESIZE = 1024
SERVER_IS_QUİT = False


clients = {}  

def sender_message(sender_name, recived_name ,message):
    for client_name, client_socket in clients.items():
        if client_name == recived_name:
            try:
                client_socket.send(f"{sender_name}: {message}".encode(ENCODER))
            except socket.error:
                print(f"Client {client_name} has disconnected. Removing client.")
                del clients[client_socket]

def handle_client(client_socket):
    client_socket.send("Welcome! Please enter your name: ".encode(ENCODER))
    client_name = client_socket.recv(BYTESIZE).decode(ENCODER)
    clients[client_name] = client_socket 

    client_socket.send(f"You are connected to the server, {client_name}.".encode(ENCODER))

    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if len(message) == 0:
                continue
            if message.lower() == "quit":
                client_socket.send("quit".encode(ENCODER))
                print(f"\r{client_name} left the chat")
                del clients[client_name]
                break

            else:
                parcalanmis_giris = message.split("> ", 1)
                if len(parcalanmis_giris) == 2:
                    recived_name, message = parcalanmis_giris
                    if recived_name in clients:
                        sender_message(client_name, recived_name ,message)
                    else :
                        client_socket.send("user not found".encode(ENCODER))
                print(f"\nSending message from {client_name} to {recived_name}: {message}")
                

        except socket.error:
            # Handle a case where the client disconnected
            print(f"Client {client_name} has disconnected. Removing client.")
            del clients[client_name]
            break

    client_socket.close()




server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print("Server is running")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()