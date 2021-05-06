import pytest
from appserver import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_fortune(app, client):
    res = client.get('/fortune/')
    assert res.status_code == 200
    output = res.get_data(as_text=True)
    assert '<pre>' in output and '</pre>' in output

def test_cowsay(app, client):
    message = 'hello'
    res = client.get('/cowsay/{}/'.format(message))
    assert res.status_code == 200
    output = res.get_data(as_text=True)
    assert message in output
    assert '<pre>' in output and '</pre>' in output

def test_cow_fortune(app, client):
    res = client.get('/cowfortune/')
    assert res.status_code == 200
    output = res.get_data(as_text=True)
    assert '<pre>' in output and '</pre>' in output
