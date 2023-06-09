# udp-server.py


import socket


HOST = "127.0.0.1"
PORT = 6000


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # allows socket re-use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the server socket
    s.bind((HOST, PORT))

    print("Listening on port {0}...".format(PORT))

    while True:
        data, addr = s.recvfrom(1024)
        print("Connected by {0}".format(addr))
        s.sendto(data, addr)
