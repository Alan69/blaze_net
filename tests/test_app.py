from werkzeug.test import EnvironBuilder
from blaze_net.app import app

def test_index():
    builder = EnvironBuilder(path='/', method='GET')
    environ = builder.get_environ()
    response = app(environ, lambda *args: None)
    assert response.status_code == 200
    assert b"Welcome to BlazeNet!" in response.data