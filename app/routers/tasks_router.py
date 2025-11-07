from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.services.task_service import search_tasks, get_task_by_id, get_all_tasks

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks(search: Optional[str] = Query(None)):
    results = search_tasks(search)
    if not results:
        return {"message": "No se encontraron tareas", "tasks": []}
    return {"tasks": results}

@router.get("/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task
