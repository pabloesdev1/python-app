from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import connection
from models.User import User
from services.users import UserService

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={ 404: {"message": "No encontrado"} },
)


@router.get("/users", response_model = List[User])
async def get_users(db = Depends(connection)):
    try:
        users: List[User] = await UserService(db).get_users()
        return JSONResponse(status_code=200, content={"result": users})
    except Exception:
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})


@router.get('/users/{id}', response_model=User)
async def get_user(id: str, db = Depends(connection)):
    try:
        user: User = await UserService(db).get_user(id)
        return JSONResponse(status_code=200, content={'result': user})
    except Exception:
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})


@router.post('/users/signup', response_model=str)
async def register(user: User, db = Depends(connection)):
    try:
        await UserService(db).register(user)
        return JSONResponse(status_code=201, content={'message': "Usuario registrado"})
    except Exception:
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})
