# fastapi_zero/exercicios.py

from http import HTTPStatus

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import (
    Message,
    UserDB,
    UserPublic,
    UserSchema,
)

router = APIRouter(prefix='/ex', tags=['exercicios'])

database_ex = []


# Use o decorator do router
@router.get('/aula_02', response_class=HTMLResponse)
def ex_aula_02():
    return """
    <html>
      <body>
        <h1> Olá Mundo! </h1>
      </body>
    </html>"""


@router.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database_ex) + 1)

    database_ex.append(user_with_id)

    return user_with_id


@router.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database_ex) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database_ex[user_id - 1] = user_with_id

    return user_with_id


@router.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database_ex) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database_ex[user_id - 1]

    return {'message': 'User deleted'}


@router.get('/users/{user_id}', response_model=UserPublic)
def read_user__exercicio(user_id: int):
    if user_id > len(database_ex) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return database_ex[user_id - 1]
