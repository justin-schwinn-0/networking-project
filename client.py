
import socket

ip = input("Server IP: ")

HOST = ip  # The server's hostname or IP address
PORT = 31312  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(command.encode())
    data = s.recv(1024)

print(f"Received {data!r}")
