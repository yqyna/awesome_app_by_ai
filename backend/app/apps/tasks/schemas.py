from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)


class TaskRead(BaseModel):
    id: int
    title: str
    completed: bool
