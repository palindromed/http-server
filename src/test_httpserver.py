import pytest


SUCCESS_RESPONSE = ("""HTTP/1.1 200 OK\r\nContent-Type: text/plain Content-Type Length: 95\r\n\r\nThis is a very simple text file. Just to show that we can serve it up. It is three lines long.""")


def test_response_ok():
    """Test response_ok function."""
    from server import response_ok
    request_tuple = ("text/plain", "This is a very simple text file. Just to show that we can serve it up. It is three lines long.".encode('ascii'))
    SUCCESS_RESPONSE = ("""HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 94\r\n\r\nThis is a very simple text file. Just to show that we can serve it up. It is three lines long.""")
    response = response_ok(request_tuple)
    response = response.decode('utf-8')
    split_response = response.split('\r\n')
    split_success = SUCCESS_RESPONSE.split('\r\n')
    assert split_response[1] == split_success[1]

def test_response_error():
    """Test response_error function."""
    from server import response_error
    response = response_error("405", "Method not allowed")
    response = response.decode('utf-8')
    slit_response = response[9:12]
    assert "405" == slit_response


def test_parse_method_0():
    """Test that server checks HTTP requests for GET method."""
    from server import parse_request
    with pytest.raises(NameError):
        argument = "BLET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)


def test_parse_method_1():
    """Test that server checks HTTP requests for correct HTTP version."""
    from server import parse_request
    with pytest.raises(AttributeError):
        argument = "GET /path/to/index.html HTTP/1.0\r\nHost: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)


def test_parse_method_2():
    """Test that server checks HTTP requests for Host header."""
    from server import parse_request
    with pytest.raises(LookupError):
        argument = "GET /path/to/index.html HTTP/1.1\r\nHoot: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)

