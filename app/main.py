from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from routers import developers, users

app = FastAPI()

origins = [
    '*'
    "http://localhost:3000", 
    "https://apivelopers.com",
    "https://www.apivelopers.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={'Message': 'Ha ocurrido un error'})
    

@app.get('/api')
def home():
    return JSONResponse(status_code=200, content={'Hello': 'World'})

app.include_router(developers.router)
app.include_router(users.router)