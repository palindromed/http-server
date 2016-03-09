# _*_ coding: utf-8 _*_
"""Create a server to echo messages."""
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
            print(msg)
            conn.sendall(response_ok())
            conn.close()
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
        server.close()


def response_ok():
    original_response ='HTTP/1.1 200 OK\nContent-Type: text/plain\n\r\nthis is a pretty minimal response'
    return original_response.encode('utf-8')
    pass


def response_error():
    pass


if __name__ == "__main__":
    server()
