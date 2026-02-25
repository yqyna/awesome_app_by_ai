from fastapi import APIRouter

from app.apps.health.views import router as health_router
from app.apps.tasks.views import router as task_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(task_router, prefix="/tasks", tags=["tasks"])
