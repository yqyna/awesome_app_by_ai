from fastapi import APIRouter

from app.apps.tasks.schemas import TaskCreate, TaskRead
from app.apps.tasks.services import create_task, list_tasks

router = APIRouter()


@router.get("", response_model=list[TaskRead])
async def task_list() -> list[TaskRead]:
    return list_tasks()


@router.post("", response_model=TaskRead, status_code=201)
async def task_create(payload: TaskCreate) -> TaskRead:
    return create_task(payload)
