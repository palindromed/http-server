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
            # response = response_ok()
            message_complete = False
            buffer_length = 8
            while not message_complete:
                part = conn.recv(buffer_length)
                decoded_part = part.decode('utf8')
                msg += decoded_part
                if len(part) < buffer_length:
                    break
            print(msg)
            response = parse_request(msg)
            conn.sendall(response)
            conn.close()
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
        server.close()
    # except:
    #         response = response_error()
    #         conn.sendall(response)
    #         conn.close()
    #         server.listen(1)
    #         conn, addr = server.accept()


def parse_request(argument):
    """Check whether message is proper HTTP request."""
    request_bits = argument.split('\n')
    print(request_bits)
    request = request_bits[0].split()
    print(request)
    host = request_bits[1].split()
    print(host)
    path = request[1]
    print(path)
    if request[0] != "GET":
        raise AttributeError('Only GET method here please.')
        # method_error = response_error("400", "Bad Request")
        # return method_error
    elif request[2] != "HTTP/1.1":
        raise AttributeError('We are only using HTTP/1.1.')
    elif host[0] != "Host:":
        raise AttributeError('You need to specify a host.')
    else:
        encode_path = response_ok(path)
        return encode_path


def response_ok(path):
    original_response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\r\n{}'.format(path)
    return original_response.encode('utf-8')


def response_error(code, reason):
    original_response = 'HTTP/1.1 {0} {1}\nContent-Type: text/plain\n\r\nWe\'ve made a huge mistake'.format(code, reason)
    return original_response.encode('utf-8')


if __name__ == "__main__":
    server()
