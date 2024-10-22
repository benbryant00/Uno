import socket
import threading

#server socket
HOST = 'localhost' # Server IP
PORT = 5555        # Server Port


#Create a socket 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = [] # List to hold connected clients

def handle_client(client_socket, address):
    print(f"New connection from {address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received from {address}: {message}")
                # Handle game logic here (broadcast moves, etc)
        except:
            print(f"Connection lost with {address}")
            client_socket.close()
            break

#Accept incoming connections 
def accept_connections():
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

print("Server is listening...")
accept_connections()