# _*_ coding: utf-8 _*_
"""Create a server to echo messages."""
import socket
import os
import io
import mimetypes

mimetypes.init()


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
            msg = b''
            message_complete = False
            buffer_length = 8
            while not message_complete:
                part = conn.recv(buffer_length)
                msg += part
                if len(part) < buffer_length:
                    break
            msg = msg.decode('utf8')
            print(msg)
            try:
                path = parse_request(msg)
                get_stuff = resolve_uri(path)
                response = response_ok(get_stuff)
            except NameError:
                response = response_error("405", "Method not allowed")
            except AttributeError:
                response = response_error("403", "Forbidden")
            except LookupError:
                response = response_error("400", "Bad Request")
            except IOError:
                response = response_error("404", "File Not Found")

            conn.sendall(response)
            conn.close()
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
        server.close()


def parse_request(argument):
    """Check whether message is proper HTTP request."""
    request_bits = argument.split('\n')
    request = request_bits[0].split()
    host = request_bits[1].split()
    path = request[1]
    if request[0] != "GET":
        raise NameError('Only GET method available here.')
    elif request[2] != "HTTP/1.1":
        raise AttributeError('We are only using HTTP/1.1.')
    elif host[0] != "Host:":
        raise LookupError('You need to specify a host.')
    else:
        return path


def resolve_uri(path):
    if os.path.isdir(path):
        prebody = os.listdir(path)
        contents = "<ul>"
        for i in prebody:
            contents += "<li>" + i + "</li>"
        contents += "</ul>"
        resolved_response = ("text/html", contents)
        return resolved_response
    elif os.path.isfile(path):
        file_type = mimetypes.guess_type(path)[0]
        file = io.open(path, "rb")
        body = file.read()
        file.close()
        resolved_response = (file_type, body)
        return resolved_response
    else:
        raise OSError


def response_ok(stuff):
    mime_type, content = stuff
    headers = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: {}\r\n'
        'Content-Length: {}\r\n'
        '\r\n'
        .format(
            mime_type,
            len(content)
        )
    )
    return headers.encode('ascii') + content


def response_error(code, reason):
    headers = (
        'HTTP/1.1 {0} {1}\r\n'
        'Content-Type: text/plain\r\n'
        '\r\nYou\'ve made a huge mistake'
        .format(code, reason)
    )
    return headers.encode('utf-8')


if __name__ == "__main__":
    server()
