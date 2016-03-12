import pytest

argument = "GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"

ERROR_RESPONSES = [(["405", "Method not allowed"], ),
                   (["403", "Forbidden"], ),
                   (["400", "Bad Request"],)]

# def test_response_ok():
#     from server import response_ok
#     result = "/test/path"
#     response = response_ok("/test/path")
#     response = response.decode('utf-8')
#     split_response = response.split('\n')
#     assert result == split_response[3]

def test_response_error():
    from server import response_error
    response = response_error("405", "Method not allowed")
    response = response.decode('utf-8')
    slit_response = response[9:12]
    assert "405" == slit_response


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


def test_good_request():
    """Test that server returns appropriate response to a good request"""
    from server import parse_request
    request = "GET /webroot/sample.txt HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"
    response = parse_request(request)
    response = response.split('\r\n')
    assert '/webroot/sample.txt' == response[3]


def test_resolve_uri():
    """Test that function parses URI, returns correct content."""
    pass


