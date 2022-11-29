
import socket

def inputCommand() -> str:

    print("Avalible commands:")
    for s in commands:
        print(s)
    print()

    tC = input("Input command:")
    while tC not in commands:
        tc = input("Command not recognized, try again")
        print("Avalible commands:")
        for s in commands:
            print(s)
        print()

    return tC

#ip = input("Server IP: ")

HOST = "127.0.1.1"#ip  # The server's hostname or IP address
PORT = 31111  # The port used by the server

commands = ["List","Read","Exit"]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
   
    
    while True:

        c = inputCommand()
        s.sendall(c.encode())
        data = s.recv(1024)

        if(c == "List"):
            print(data.decode())
        elif(c == "Read"):
            sel = input(data.decode())
            s.sendall(sel.encode())
            s.recv(1024)

        
        if(c == "Exit"):
            break



