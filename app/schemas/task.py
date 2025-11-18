from pydantic import BaseModel
from typing import Optional

# Shared Task Properties
class TaskBase(BaseModel):
    title:str
    description:Optional[str] = None

# For Task Creation
class CreateTask(TaskBase):
    pass

# For Task Update (Partial)
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None

# Returned to the Client
class TaskOut(TaskBase):
    id:int
    is_completed:bool
    owner_id:int

    class Config:
        orm_mode = True