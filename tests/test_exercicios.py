from http import HTTPStatus


def test_ex_aula_02_ola_mundo_em_html(client):
    response = client.get('/ex_aula_02')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo! </h1>' in response.text
