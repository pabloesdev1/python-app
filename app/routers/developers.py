from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import connection
from models.Developer import Developer
from models.Skill import Skill
from services.developers import DeveloperSevice

router = APIRouter(
    prefix="/api",
    tags=["developers"],
    responses={ 404: {"message": "No encontrado"} },
)


@router.get("/developers", response_model = List[Developer])
async def get_developers(db = Depends(connection)):
    try:
        developers: List[Developer] = await DeveloperSevice(db).get_developers()
        return JSONResponse(status_code=200, content={"result": developers})
    except Exception:
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})


@router.get('/developers/{id}', response_model=Developer)
async def get_developer(id: str, db = Depends(connection)):
    try:
        developer: Developer = await DeveloperSevice(db).get_developer(id)
        return JSONResponse(status_code=200, content={'result': developer})
    except Exception:
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})


@router.get('/developers/{id}/skills', response_model=List[Skill])
async def get_skills(id: str, db = Depends(connection)):
    try:
        skills = await DeveloperSevice(db).get_skills(id)
        return JSONResponse(status_code=200, content={'result': skills})
    except Exception:
        return JSONResponse(status_code=500, content={'message': 'Ha ocurrido un error'})


@router.post('/developers', response_model=str)
async def create_developer(developer: Developer, db = Depends(connection)):
    try:
        await DeveloperSevice(db).create_developer(developer)
        return JSONResponse(status_code=201, content={'message': "Desarrollador registrado"})
    except Exception:
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})


@router.put('/developers/{id}', response_model=str)
async def update_developer(data: Developer, id: str, db = Depends(connection)):
    try:
        await DeveloperSevice(db).update_developer(id, data)
        return JSONResponse(status_code=201, content={'message': "Desarrollador modificado"})
    except Exception:
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})


@router.delete('/developers/{id}', response_model=str)
async def delete_developer(id: str, db = Depends(connection)):
    try:
        await DeveloperSevice(db).delete_developer(id)
        return JSONResponse(status_code=200, content={'message': "Desarrollador eliminado"})
    except Exception:
        return JSONResponse(status_code=500, content={'message': "Ha ocurrido un error"})