from fastapi import FastAPI

from app.config.settings import settings
from app.config.urls import api_router
from app.core.exception_handlers import register_exception_handlers


def create_application() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        version=settings.version,
        docs_url="/docs",
        redoc_url="/redoc",
    )
    app.include_router(api_router, prefix=settings.api_prefix)
    register_exception_handlers(app)
    return app


app = create_application()
