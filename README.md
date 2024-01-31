# Python Chat Application with Socket

This project aims to implement a simple chat application with Python using sockets. It enables text-based communication between clients and the server.

## Use

- `client.py`: Client side code. Can connect to the server on another device and chat.
- `server.py`: Main server side code. It allows clients to connect and communicate.


## Dependencies

-Python 3.x

## Setup

1. Clone or download the project files to your computer.
2. <pre>pip install -r requirements.txt</pre>
3. Assign the IP and port information of the computer on which the server will run to the HOST_IP and HOST_PORT variables in the `chat_server.py` file.
4. Run `chat_server.py` to start the server side.
5. Enter the server information into the DEST_IP and DEST_PORT variables in `chat_client.py`
6. Start `chat_client.py` to start the client side and connect to the server.
7. Enter username on the client side and start chatting.

## Note

- The user must use the `quit` command to exit the conversation.
- To send a message, write as follows: <pre>recipient_name > message</pre>