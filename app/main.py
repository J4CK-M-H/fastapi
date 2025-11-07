# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routers import tasks_router

# app = FastAPI(title="API de Búsqueda de Tareas")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # <- puedes restringirlo si deseas
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Registrar los routers de tasks
# app.include_router(tasks_router.router)

# @app.get("/")
# def root():
#     return {"message": "API de Tareas"}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tasks_router

# Obtén la URL de tu frontend de Netlify.
# ¡REEMPLAZA ESTE VALOR CON TU DOMINIO REAL DE NETLIFY!
NETLIFY_URL = "https://subtle-dasik-0be649g.netlify.app/" 

app = FastAPI(title="API de Búsqueda de Tareas")

app.add_middleware(
    CORSMiddleware,
    # Permitir SOLO a tu frontend de Netlify acceder a la API
    allow_origins=[NETLIFY_URL], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers de tasks
app.include_router(tasks_router.router)

@app.get("/")
def root():
    return {"message": "API de Tareas"}