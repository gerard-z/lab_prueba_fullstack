from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import router_base
import uvicorn

# iniciar la aplicacion, conectandose a la base de datos
def init_app():
    app = FastAPI(
        title="TCG Backend",
        version="0.0.1",
        description="API para el backend de la aplicación TCG como proyecto de prueba",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.include_router(router_base.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173", "http://localhost:8080", "http://localhost"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)