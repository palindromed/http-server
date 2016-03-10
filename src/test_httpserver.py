import pytest

argument = "GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"


def test_response_ok():
    from server import response_ok
    # response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\r\nHere\'s your response.'
    # response = response.encode('utf-8')
    result = "/test/path"
    response = response_ok("/test/path")
    response = response.decode('utf-8')
    split_response = response.split('\n')
    assert result == split_response[3]


# def test_response_error():
#     from server import response_error
#     response = 'HTTP/1.1 500 Internal Server Error\nContent-Type: text/plain\n\r\nWe\'ve made a huge mistake'
#     response = response.encode('utf-8')
#     assert response_error() == response


# def test_server():
#     # The server needs to be running for this test
#     from client import client
#     response = client('A message')
#     response = response.split('\n')
#     assert response == ['HTTP/1.1 200 OK', 'Content-Type: text/plain', '\r', "Here's your response."]


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
