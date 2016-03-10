import pytest

argument = "GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"


# def test_response_ok():
#     from server import response_ok
#     response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\r\nHere\'s your response.'
#     response = response.encode('utf-8')
#     assert response_ok() == response


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


def test_parse_method():
    """Test that server checks HTTP requests for GET method."""
    from server import parse_request
    with pytest.raises(AttributeError):
        argument = "BLET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)
