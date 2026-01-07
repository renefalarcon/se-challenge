from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)

def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(status_code=404, content={"Obs": "Usuario no encontrado"})

def user_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(status_code=409, content={"Obs": "Usuario ya existe"})
