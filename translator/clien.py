import socket

lang = input("enter use lang: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8881))

while True:
    text = input("enter text: ")
    
    if text == "!q":
        s.close()
        break
    
    s.send(f"{lang}: {text}".encode())
    output = s.recv(1024).decode()
    print(output)
