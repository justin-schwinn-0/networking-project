# Upper case letters are to the server, lower case leteres are the responses
#
# L: request list
# l: list data   
#
#

import socket
import sys

hn = socket.gethostname()

host = socket.gethostbyname(hn)

#host = "127.0.0.1"
ClientPort = 31111
ServerPort = 31123

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    client.bind((host,ClientPort))

    print(host)
    print(ClientPort)
    client.listen()

    connC , addrC = client.accept()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect((host,ServerPort))

        with connC:
            while True:
                data = connC.recv(1024)
            
                if(data  == b'List'):

                    print("getting list...")
                    
                    server.sendall("L".encode())



                    serverData = server.recv(1024)

                    print("forwarding list...")



                    connC.sendall(serverData)
                elif(data == b'Read'):
                    connC.sendall("Select file: ".encode())
                    selection = connC.recv(1024)

                    print("getting file contents...")
                    send = "R" + selection.decode()
                    server.sendall(send.encode())

                    serverData = server.recv(1024)
                    connC.sendall(serverData)
                    print("forwarding file contents...")
                
                else:
                    connC.sendall("unknown command".encode())

                if not data:
                    break