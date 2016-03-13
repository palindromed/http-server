# _*_ coding: utf-8 _*_

"""Create sample client to test echo server functionality."""
import sys
import socket


def client(message):
    specs = socket.getaddrinfo('127.0.0.1', 5000)
    stream_specs = [i for i in specs if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_specs[:3])
    client.connect(stream_specs[-1])
    client.sendall(message.encode("utf8"))

    msg = b''
    message_complete = False
    buffer_length = 8
    while not message_complete:
        part = client.recv(buffer_length)
        msg += part
        if len(part) < buffer_length:
            client.close()
            break
    msg = msg.decode('utf8')
    return msg


if __name__ == "__main__":
    client(sys.argv[1])
