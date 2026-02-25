from app.apps.tasks.repositories import TaskRepository
from app.apps.tasks.schemas import TaskCreate, TaskRead
from app.core.exception_handlers import DomainError

repo = TaskRepository()


def list_tasks() -> list[TaskRead]:
    return repo.list_tasks()


def create_task(payload: TaskCreate) -> TaskRead:
    if payload.title.strip() == "":
        raise DomainError("Task title must not be blank.")
    return repo.create_task(payload)
