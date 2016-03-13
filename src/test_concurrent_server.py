import pytest

SUCCESS_RESPONSE = ("""HTTP/1.1 200 OK\r\nContent-Type: text/plain Content-Type Length: 95\r\n\r\nThis is a very simple text file. Just to show that we can serve it up. It is three lines long.""")

DIR_RESP = (b'<ul><li>.DS_Store</li><li>a_web_page.html</li>'
            b'<li>images</li><li>make_time.py</li>'
            b'<li>sample.txt</li></ul>')


def test_response_ok():
    """Test response_ok function."""
    from concurrent_server import response_ok
    request_tuple = ("text/plain", "This is a very simple text file. Just to show that we can serve it up. It is three lines long.".encode('ascii'))
    SUCCESS_RESPONSE = ("""HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 94\r\n\r\nThis is a very simple text file. Just to show that we can serve it up. It is three lines long.""")
    response = response_ok(request_tuple)
    response = response.decode('utf-8')
    split_response = response.split('\r\n')
    split_success = SUCCESS_RESPONSE.split('\r\n')
    assert split_response[1] == split_success[1]


def test_response_error():
    """Test response_error function."""
    from concurrent_server import response_error
    response = response_error("405", "Method not allowed")
    response = response.decode('utf-8')
    slit_response = response[9:12]
    assert "405" == slit_response


def test_parse_method_0():
    """Test that server checks HTTP requests for GET method."""
    from concurrent_server import parse_request
    with pytest.raises(NameError):
        argument = "BLET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)


def test_parse_method_1():
    """Test that server checks HTTP requests for correct HTTP version."""
    from concurrent_server import parse_request
    with pytest.raises(AttributeError):
        argument = "GET /path/to/index.html HTTP/1.0\r\nHost: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)


def test_parse_method_2():
    """Test that server checks HTTP requests for Host header."""
    from concurrent_server import parse_request
    with pytest.raises(LookupError):
        argument = "GET /path/to/index.html HTTP/1.1\r\nHoot: www.mysite1.com:80\r\n\r\n"
        parse_request(argument)


def test_good_request():
    """Test that a well formed request gets path returned from parsing to a good request"""
    from concurrent_server import parse_request
    request = "GET /webroot/sample.txt HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"
    assert parse_request(request) == '/webroot/sample.txt'


def test_resolve_uri():
    """Test that function resolves path and returns directory content."""
    from concurrent_server import resolve_uri
    path = "/Users/hannahkrager/http-server/webroot/"
    assert resolve_uri(path) == ("text/html", DIR_RESP)


def test_file_not_found():
    """Test that a directory not found raises an error."""
    from concurrent_server import resolve_uri
    with pytest.raises(OSError):
        resolve_uri('/webroot.html/')


def test_file_found():
    """Test that if a file is found, it will be returned."""
    from concurrent_server import resolve_uri
    path = "/Users/hannahkrager/http-server/webroot/sample.txt"
    body = (b"This is a very simple text file.\n"
            b"Just to show that we can serve it up.\n"
            b"It is three lines long.\n"
            )
    assert resolve_uri(path) == ("text/plain", body)
