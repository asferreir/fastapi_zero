# fastapi_zero/exercicios.py

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


# Use o decorator do router
@router.get('/ex_aula_02', response_class=HTMLResponse)
def ex_aula_02():
    return """
    <html>
      <body>
        <h1> Olá Mundo! </h1>
      </body>
    </html>"""
