from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schema import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/ex_aula_02', response_class=HTMLResponse)
def ex_aula_02():
    return """
    <html>
      <body>
        <h1> Olá Mundo! </h1>
      </body>
    </html>"""
