# _*_ coding: utf-8 _*_


def test_i_0():
    from client import client
    msg = "this is a test too"
    assert client(msg) == msg


def test_short():
    from client import client
    msg = 'hi'
    assert client(msg) == msg


def test_exact():
    from client import client
    msg = '12345678'
    assert client(msg) == msg


def test_non_ascii():
    from client import client
    msg = 'über!'
    assert client(msg) == msg
