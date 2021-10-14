import socket
import threading
import os


IP = '192.168.43.144'
PORT = 9909

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen()
    conn, addr = server.accept()
    PATH = os.getcwd()
    conn.send(PATH.encode("utf-8"))
    while True:
        data = conn.recv(1024).decode('utf-8')
        if 'ls' in data:
            data = data.split("@")
            PATH = data[0]
            list = str(os.listdir(PATH))
            conn.send(list.encode("utf-8"))
        elif "cd" in data:
            data = data.split("@")
            PATH = data[0]
            print(PATH)
            data = data[1]
            print(data)
            data = data.split(" ")
            data = data[1]
            print(data)
            if data == "..":
                PATH = PATH.split("/")
                PATH = PATH[-1]
                print(PATH)
                New = os.getcwd()
                PATH = New.replace(PATH, "")
                print(PATH)
                conn.send(PATH.encode("utf-8"))
        else:
            main()

main()