from app.apps.health.schemas import HealthResponse
from app.config.settings import settings


def get_health_status() -> HealthResponse:
    return HealthResponse(status="ok", environment=settings.environment)
