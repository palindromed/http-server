# _*_ coding: utf-8 _*_
"""Create a server to echo messages."""
import socket
import sys


def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)  # xxx
    conn, addr = server.accept()

    while True:
        msg = ''
        message_complete = False
        buffer_length = 8
        while not message_complete:
            part = conn.recv(buffer_length)
            decoded_part = part.decode('utf8')
            msg += decoded_part
            print(msg)
            if len(part) < buffer_length:
                break  #  send back msg
        conn.sendall(msg.encode("utf8"))
        server.listen(1)
        conn, addr = server.accept()



    # start running server
    # keep running and sending responses
    # crtl-d cleanly exit
    # flag for dealing with server crashes
    # accept msg
    # echo msg
    # close conn
if __name__ == "__main__":
    server()
