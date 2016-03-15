# _*_ coding: utf-8 _*_
"""Create a server that can handle concurrent messages."""
from server import parse_request, resolve_uri, response_ok, response_error


def server(socket, address):

    msg = b''
    buffer_length = 8
    message_complete = False
    while not message_complete:
        data = socket.recv(buffer_length)
        msg += data
        if len(data) < buffer_length:
            break
    msg = msg.decode('utf-8')
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
    socket.sendall(response)
    socket.close()


if __name__ == "__main__":
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 5000), server)
    print('Starting server on port 5000')
    server.serve_forever()
