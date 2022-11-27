import socket
import sys

hn = socket.gethostname()

host = socket.gethostbyname(hn)

#host = "127.0.0.1"
port = 30312

print(f"IP:{host}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()

    conn , addr = s.accept()

    with conn:
        print(f"Connected to: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

