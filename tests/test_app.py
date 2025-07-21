from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo_e_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


def test_ex_aula_02_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/ex_aula_02')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo! </h1>' in response.text
