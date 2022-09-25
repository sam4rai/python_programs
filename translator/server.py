import socket
from main import get_translate

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 8881))
s.listen()

client, addr = s.accept()
print(f"{addr} connect")

while True:
    
    text = client.recv(1024).decode().split(": ")
    src = text[0]
    mess = text[1]
    translation = get_translate(text=mess, src = src)
    client.send(f"Translation: {translation}".encode())
