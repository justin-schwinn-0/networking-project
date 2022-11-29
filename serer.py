import socket
import os
hn = socket.gethostname()

host = socket.gethostbyname(hn)

#host = "127.0.0.1"
port = 31123

print(host)
print(port)

fileList = os.listdir('files')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()

    conn , addr = s.accept()

    with conn:
        print(f"Connected to: {addr}")
        while True:
            data = conn.recv(1024).decode()
            print(data)
            if(len(data) < 1):
                break
            if(data[0] == 'L'):

                
                dataList = ""

                print(fileList)

                for str in fileList:
                    dataList += str + "\n"


                print(dataList)
                print(f"sending list of {len(dataList)}...")


                conn.sendall(dataList.encode())
            elif(data[0] == 'R'):
                filename = data[1:]

                if(filename in fileList):
                    print("File found...")

                    path = "files/"+filename
                    fd = open(path).read()

                    conn.sendall(fd.encode())
                    print(f"Sending {len(fd)} bytes")
                else:
                    conn.sendall("file not found".encode())
            else:
                conn.sendall("Server doesn't know command".encode())

