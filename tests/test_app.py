from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_should_return_ok_e_ola_mundo():
    client = TestClient(app)  # arrange
    response = client.get('/')  # act
    assert response.status_code == HTTPStatus.OK  # assert
    assert response.json() == {'message': 'Hello World'}  # assert
