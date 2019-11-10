import socket

def sendData():
    print("Enter the Ip Address of the host you want to connect!")
    HOST = input()
    print("Enter the Port number of the connecting PC")
    PORT = input()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, int(PORT)))
        s.sendall('Hello, world')
        data = s.recv(1024)

    print('Received', repr(data))

sendData()