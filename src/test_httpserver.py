
def test_response_ok():
    from server import response_ok
    response = 'HTTP/1.1 200 OK\nContent-Type: text/plain\n\r\nHere\'s your response.'
    response = response.encode('utf-8')
    assert response_ok() == response


def test_response_error():
    from server import response_error
    response = 'HTTP/1.1 500 Internal Server Error\nContent-Type: text/plain\n\r\nWe\'ve made a huge mistake'
    response = response.encode('utf-8')
    assert response_error() == response

