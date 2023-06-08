# tcp-server.py


import socket


HOST = "127.0.0.1"
PORT = 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # allows socket re-use
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the server socket
    s.bind((HOST, PORT))

    # listen on the specified host + port
    s.listen()
    print("Listening on port {0}...".format(PORT))

    conn, addr = s.accept()
    print("Client connected")

    with conn:
        print("Connected by {0}".format(addr))
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
