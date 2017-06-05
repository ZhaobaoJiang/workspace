#!/usr/bin/env python2.7
#coding:utf-8
import socket

def handle_request(client):
     buf = client.recv(1024)
     client.send("HTTP/1.1 200 OK\r\n")
     client.send("Content-Type:text/html \r\n\r\n")
     client.send("<a href='www.baidu.com'>Hello World!</a>")

def main():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("localhost",8080))
    sock.listen(5)

    while True:
         connection,address = sock.accept()
         handle_request(connection)
         connection.close()

if __name__ == "__main__":
    main()
