import socket 
import tkinter as tk
from threading import Thread

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost' # Server IP
PORT = 5555        # Server Port
client_socket.connect((HOST, PORT))

# Function to send a messafe to the server
def send_message(message):
    client_socket.send(message.encode('utf-8'))


# GUI logic (Tkinter)
def start_game():
    root = tk.Tk()
    root.title("UNO Game")

    # Example button for playing a card
    play_card_button = tk.Button(root, text="Play Card", command=lambda: send_message("Playing card"))
    play_card_button.pack()

    root.mainloop()

# Thread to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Server says {message}")
        except:
            print(f"Connection to server lost.")
            break

# Start the game and message receiving thread
Thread(target=receive_messages).start()
start_game()