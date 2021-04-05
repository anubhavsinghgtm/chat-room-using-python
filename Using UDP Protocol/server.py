import socket

myp = socket.SOCK_DGRAM
afn = socket.AF_INET

s = socket.socket(afn,myp)

ip = "192.168.43.57"
port = 1234
s.bind((ip,port))

while True:
    x = s.recvfrom(1024)
    ip = x[1][0]
    res=x[0].decode()
    if(res=='exit'):
        print()
        print('==== Exiting the program ====')
        break;
    else:
        print(ip+ ': ' + res)

﻿