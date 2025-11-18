from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.task import CreateTask, TaskUpdate, TaskOut
from app.tasks import crud_task
from app.auth.routes import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tasks", tags=["tasks"])

# Create a new task
@router.post("/", response_model=TaskOut)
def create_task(payload:CreateTask, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    task = crud_task.create_task(db, payload.title, payload.description, current_user.id)

    return task

# Get all tasks for current user
@router.get("/", response_model=List[TaskOut])
def read_tasks(db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    return crud_task.get_tasks(db,current_user.id)

# Get single task by ID
@router.get("/{task_id}",response_model=TaskOut)
def read_task(task_id:int, db:Session = Depends(get_db), current_user:User = Depends(get_current_user)):
    task = crud_task.get_task(db, current_user.id, task_id)

    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found!")
    
    return task

# Update a task
@router.patch("/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    task = crud_task.get_task(db, current_user.id, task_id)
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task not found")
    
    task = crud_task.update_task(db, task, title=payload.title, description=payload.description, is_completed=payload.is_completed)

    return task

# Delete a task
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    
    task = crud_task.get_task(db, current_user.id, task_id)
    
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    
    crud_task.delete_task(db, task)
    
    return {"ok": True}
