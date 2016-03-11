# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest

FAILED_MESSAGES = [
    (u"BLET / HTTP/1.1\r\nHost: localhost:5000", NameError),
    (u"GET / HTTP/1.0\r\nHost: localhost:5000", AttributeError),
    (u"GET / HTTP/1.1\r\nHoot", LookupError)
]

ERROR_RESPONSE = [
    ("200", u"HTTP/1.1 200 OK\r\n"),
    ("400", u"HTTP/1.1 400 Bad Request\r\n"),
    ("404", u"HTTP/1.1 404 File Not Found\r\n"),
    ("405", u"HTTP/1.1 405 Method Not Allowed\r\n"),

]


SUCCESS_RESPONSE = [(u"GET / HTTP/1.1\r\nHost: localhost:5000", "/")]


argument = "GET /path/to/index.html HTTP/1.1\r\nHost: www.bananagrabber.com:80\r\n\r\n"

ERROR_RESPONSES = [(["405", "Method not allowed"], ),
                   (["403", "Forbidden"], ),
                   (["400", "Bad Request"],)]



def test_response_ok():
    from server import response_ok
    result = "/test/path"
    response = response_ok("/test/path")
    response = response.decode('utf-8')
    split_response = response.split('\n')
    assert result == split_response[3]

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
        argument = "BLET /path/to/index.html HTTP/1.1\r\nHost: www.bananagrabber.com:80\r\n\r\n"
        parse_request(argument)


def test_parse_method_1():
    """Test that server checks HTTP requests for correct HTTP version."""
    from server import parse_request
    with pytest.raises(AttributeError):
        argument = "GET /path/to/index.html HTTP/1.0\r\nHost: www.bananagrabber.com:80\r\n\r\n"
        parse_request(argument)


def test_parse_method_2():
    """Test that server checks HTTP requests for Host header."""
    from server import parse_request
    with pytest.raises(LookupError):
        argument = "GET /path/to/index.html HTTP/1.1\r\nHoot: www.bananagrabber.com:80\r\n\r\n"
        parse_request(argument)


def test_resolve_uri():
    """Test that function parses URI, returns correct content."""
