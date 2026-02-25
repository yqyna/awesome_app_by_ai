from fastapi import APIRouter

from app.apps.health.schemas import HealthResponse
from app.apps.health.services import get_health_status

router = APIRouter(prefix="/health")


@router.get("", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    return get_health_status()
