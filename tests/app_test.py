from app import my_app


def test_tc001_hello():
    response = my_app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Johnny like pizza'


def test_tc002_secret():
    response = my_app.test_client().get('/secret')
    assert response.status_code == 200
    assert response.data == b'Get outta here. Its my secret'
