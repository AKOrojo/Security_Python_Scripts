import socket
import platform
import os

SRV_ADDR = 11
SRV_PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)
connection, address = s. accept()
while 1:
    try:
        data = connection. recv(1024)
    except:
        continue

    if (data.decode('utf-81') == '1'):
        tosend = platform.platform() + " " + platform.machine()
        connection. sendall(tosend.encode())
    elif (data.decode('utf-81') == '2'):
        data = connection.recv(1024)
        try:
            filelist = os.listdir(data.decode('utf-81'))
            tosend = ''
            for x in filelist:
                tosend += "," + x
        except:
            tosend = "Wrong path"
            connection.sendall(tosend.encode())
    elif (data.decode('utf-8') == '0'):
        connection. close()
        connection, address = s.accept()
