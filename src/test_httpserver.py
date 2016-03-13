
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


def test_server():
    # The server needs to be running for this test
    from client import client
    response = client('A message')
    response = response.split('\n')
    assert response == ['HTTP/1.1 200 OK', 'Content-Type: text/plain', '\r', "Here's your response."]
