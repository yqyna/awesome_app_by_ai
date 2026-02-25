from app.apps.tasks.schemas import TaskCreate, TaskRead


class TaskRepository:
    """In-memory repository to mimic ORM service boundaries."""

    def __init__(self) -> None:
        self._tasks: list[TaskRead] = []
        self._next_id = 1

    def list_tasks(self) -> list[TaskRead]:
        return self._tasks

    def create_task(self, payload: TaskCreate) -> TaskRead:
        task = TaskRead(id=self._next_id, title=payload.title, completed=False)
        self._tasks.append(task)
        self._next_id += 1
        return task
