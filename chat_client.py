import socket
import threading

DEST_IP = "192.168.25.201"
DEST_PORT = 50007
ENCODER = "utf-8"
BYTESIZE = 1024
IS_QUIT = True

def recive_mesage(conn):
    global IS_QUIT
    while IS_QUIT:
        message = input("")
        conn.send(message.encode(ENCODER))
        if message == "quit":
            print("ending the chat")
            IS_QUIT = False
            return

def send_mesage(conn):
    global IS_QUIT
    while IS_QUIT:
        message = conn.recv(BYTESIZE).decode(ENCODER)
        if message == "quit":
            conn.send("quit".encode(ENCODER))
            print("ending the chat")
            IS_QUIT = False
        else:
            print(f"Received: {message}")
    return
            

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

send_thread = threading.Thread(target=send_mesage, args=(client_socket,))
recived_thread = threading.Thread(target=recive_mesage, args=(client_socket,))

send_thread.start()
recived_thread.start()

send_thread.join()
recived_thread.join()


client_socket.close()
