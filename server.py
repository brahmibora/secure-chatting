import socket
import threading
from encryption import decrypt
from datetime import datetime

host = '127.0.0.1'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
names = []

def log_message(message):
    with open("chat.log", "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

def broadcast(message, _client=None):
    for client in clients:
        if client != _client:
            client.send(message)

def handle(client):
    while True:
        try:
            encrypted_msg = client.recv(2048).decode()
            msg = decrypt(encrypted_msg)
            log_message(msg)
            broadcast(encrypted_msg, client)
        except:
            index = clients.index(client)
            name = names[index]
            log_message(f"{name} disconnected.")
            clients.remove(client)
            names.remove(name)
            client.close()
            break

def receive():
    while True:
        client, _ = server.accept()
        client.send("NAME?".encode())
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)
        log_message(f"{name} connected.")
        broadcast(f"{name} joined the chat.".encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server started...")
receive()
