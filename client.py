import socket
import threading
import os 

IP = '192.168.43.144'
PORT = 9909

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    PATH = client.recv(1024).decode('utf-8')
    while True:
        msg = input(f"{PATH}$ ")
        if msg == 'ls':
            msg = f"{PATH}@{msg}"
            client.send(msg.encode('utf-8'))
            result = client.recv(1024).decode('utf-8')
            print(result)
        elif "cd" in msg:
            msg = f"{PATH}@{msg}"
            client.send(msg.encode('utf-8'))
            PATH = client.recv(1024).decode('utf-8')
        else:
            main()
        

main()