from typing import List, Optional
from app.data.tasks import tasks
from app.models.task_model import Task

def get_all_tasks() -> List[Task]:
    return tasks

def search_tasks(search: Optional[str] = None) -> List[Task]:
    results = tasks


    if search:
       
        search_lower = search.lower()
        
        results = [
                t for t in results
                if search_lower in t["title"].lower()
                or search_lower in t["priority"].lower()
                or str(t["id"]) == search
            ]

    return results

def get_task_by_id(task_id: int) -> Optional[Task]:
    for t in tasks:
        if t["id"] == task_id:
            return t
    return None
