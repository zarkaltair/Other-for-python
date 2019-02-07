import socket


host = '127.0.0.1'
port = 9000

s = socket.socket()
s.connect((host, port))
print('You are connected by server\nIf you are want to disconnect please enter exit.')


str = input("Enter data: ")

while str != 'exit':
    s.send(str.encode())

    data = s.recv(1024)
    data = data.decode()
    print("From server: " + data)

    str = input("Enter data: ")

s.close