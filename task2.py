#!/usr/bin/env python

import socket
import time


nextPort = 3010


page = ""


s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.10.73.25" , 3010))
s.sendall(b"GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\nConnection: close\r\n\r\n")

while True:

    data = s.recv(1024)

    if not data:
        break

    page = page + data.decode()



    #print(page)

start = page.index("Its currenly on port") + 55
end = page.index("Refresh this page and it will update") - 10

nextPort = page[start:end]

page = ""

print("waiting for port 1337 to open, current port: "+ nextPort)


#get next port

answer = 0

while nextPort != "9765":

    try:

        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #print("connecting to "+nextPort)

        s.connect(("10.10.73.25" , int(nextPort)))
        s.sendall(b"GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\nConnection: close\r\n\r\n")


        while True:

            data = s.recv(1024)

            if not data:
                break

            page = page + data.decode()

        message = page[154:]

        print("port " + nextPort + ": " + message)

        nextPort = message.split()[2]
        page = ""
        time.sleep(1)

   
    except:
        time.sleep(0.1)

print("answer is: "+ answer)
