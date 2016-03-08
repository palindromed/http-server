# _*_ coding: utf-8 _*_
"""Create a server to echo messages."""
from __future__ import unicode_literals
import socket


def server():
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()

    try:
        while True:
            msg = ''
            message_complete = False
            buffer_length = 8
            while not message_complete:
                part = conn.recv(buffer_length)
                decoded_part = part.decode('utf8')
                msg += decoded_part
                if len(part) < buffer_length:
                    break
            conn.sendall(msg.encode("utf8"))
            conn.close()
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
        server.close()

    # crtl-d cleanly exit
if __name__ == "__main__":
    server()
