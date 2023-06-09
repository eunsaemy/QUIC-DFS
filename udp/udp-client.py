# udp-client.py


import socket
import time


HOST = "127.0.0.1"
PORT = 6000


def send_msg():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # allows socket re-use
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # connect to the server socket
        s.connect((HOST, PORT))

        # send data
        print("Sending data")
        s.sendall(b"Hello world")

        # receive data
        print("Receiving data")
        data, addr = s.recvfrom(1024)

        # echo data
        print("Received:", data.decode())


def main():
    start_time = time.time()
    send_msg()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time: {0} seconds".format(elapsed_time))


if __name__ == "__main__":
    main()
