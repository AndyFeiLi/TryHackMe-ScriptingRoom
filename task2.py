#!/usr/bin/env python

import socket
import time


nextPort = 3010


page = ""

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.10.38.175" , 3010))
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

#get next port

while True:

    try:

        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #print("connecting to "+nextPort)

        s.connect(("10.10.38.175" , int(nextPort)))
        s.sendall(b"GET / HTTP/1.1\r\nHost: webcode.me\r\nAccept: text/html\r\nConnection: close\r\n\r\n")


        while True:

            data = s.recv(1024)

            if not data:
                break

            page = page + data.decode()

        if page == "TOP":
            break


        message = page[154:]

        print("port " + nextPort + ": " + message)

        nextPort = message.split()[2]
        page = ""
        time.sleep(1)
    except:
        time.sleep(0.1)
