from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.task import Task

# Create a new task
def create_task(db:Session, title:str, description:Optional[str], owner_id:int) -> Task:
    task = Task(title=title, description=description, owner_id=owner_id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Get all tasks for a User
def get_tasks(db:Session, owner_id:int) -> List[Task]:
    return db.query(Task).filter(Task.owner_id == owner_id).all()

# Get single task by id
def get_task(db:Session, owner_id:int, task_id:int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == owner_id).first()

# Update Task
def update_task(db:Session, task:Task, title:str = None, description:str = None, is_completed:bool = None) -> Task:
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if is_completed is not None:
        task.is_completed = is_completed
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Delete task
def delete_task(db:Session, task:Task):
    db.delete(task)
    db.commit()
