import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(5)
while True:
    c, addr = s.accept()
    print("addr:", addr)
    c.send("welcome to DP")
    c.close()
