from app import my_app


def test_tc001_hello():
    response = my_app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Johnny like pizza'
