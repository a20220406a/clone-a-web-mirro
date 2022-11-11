import socket
import ssl
import threading
import multiprocessing


server = socket.socket()
server.bind(("0.0.0.0", 80))
server.listen(80)

def do(fd,):
    g = b''
    c = fd.recv(2)
    while c:
        g = g + c
        c = fd.recv(2)
    cli = socket.socket()
    #li.connect(("harbor.sugn.top",443))
    cli2 = ssl.wrap_socket(cli)
    cli2.connect(("harbor.sugn.top",443))
    #cli2.connect(("192.168.1.1",80))
    cli2.send(g)
    d = b''
    f = cli2.recv(2)
    while d:
        d = d + f
        f = cli2.recv(2)
    cli2.close()
    fd.send(d)
    fd.close()



while True:
    fd,(addr,port) = server.accept()
    print(addr,port)
    #ig = B""
    #c = fd.recv(32)
    threading.Thread(target=do,args=(fd,)).start()
    print("is async d.")
