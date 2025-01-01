from typing import Union
from fastapi import FastAPI
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

    return app

app = init_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)