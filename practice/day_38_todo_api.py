from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime

app = FastAPI(
    title='To-Do API',
    description='Full CRUD To-Do API',
    version='1.0.0'
)

todos = []
next_id = 1

class TodoCreate(BaseModel):
    title : str =Field(...,min_length=1,max_length=100)
    description: Optional[str] = Field(None,max_length=500)
    priority: str = Field("medium",pattern="^(low|medium|high)$")

class TodoUpdate(BaseModel):
    title: str = Field(None,min_length=1,max_length=100)
    description: Optional[str] = Field(None,max_length=100)
    priority:Optional[str] = Field(None,pattern="^(low|medium|high)$")
    completed: Optional[bool] = None

class Todo(BaseModel):
    id:int
    title: str
    description: Optional[str] = None
    priority:str
    completed:bool
    created_at:str

@app.get("/todos")
def list_todos(completed:Optional[bool] = None ,priority:Optional[str] = None):
    result = todos
    if completed is not None:
        result = [t for t in result if t["completed"]==completed]
    if priority is not None:
        result = [t for t in result if t["priority"]== priority]

    return{
        "total":len(result),
        "filters":{"completed":completed,"priority":priority},
        "todos":result
    }

@app.get('/todo/{tod_id}')
def get_todo(todo_id:int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todos
    raise HTTPException(status_code=404,detail=f"Todo {todo_id} not found")

@app.post('/todo',status_code=201)
def create_todo(todo:TodoCreate):
    global next_id

    new_todo = {
        "id":next_id,
        "title":todo.title,
        "description":todo.description,
        "priority":todo.priority,
        "completed":False,
        "created_at":datetime.now().isoformat()
    }
    todos.append(new_todo)
    next_id+=1
    return{"message":"Tudo created","todo":new_todo}

@app.put('/todo/{todo_id}')
def update(todo_id:int,update:TodoUpdate):
    for todo in todos:
        if todo["id"] == todo_id:
            if update.title is not None:
                todo["title"] = update.title
            if update.description is not None:
                todo["description"] = update.description
            if update.priority is not None:
                todo["priority"] = update.priority
            if update.completed is not None:
                todo["completed"] = update.completed
            return{'message':'Todo update' ,'todo':todo}
    raise HTTPException(status_code=404,detail=f"Todo {todo_id}not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for i,todo in enumerate(todos):
        if todo["id"] == todo_id:
            removed = todos.pop(i)
            return{'message':'Todo update' ,'todo':removed}
    raise HTTPException(status_code=404,detail=f"Todo {todo_id}not found")

@app.get(",stats")
def get_stats():
    total = len(todos)
    done = sum(1 for t in todos if t["completed"])
    pending = total - done

    return{
        "total":total,
        "completed":done,
        "pending":pending,
        "completion_rate":f"{(done/total *100) if total > 0 else 0:.1f}%"
    }