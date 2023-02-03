from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "hey its jadaaa"}

app = FastAPI()
origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_database = []
@app.get("/todos")
async def get_all_todos():
    return fake_database

@app.post("/todos")
async def create_todo(request: Request):
    todo = await request.json()
    fake_database.append(todo)
    return todo
    
@app.get("/todos/{id}")
async def get_todoid(id: int):
    return fake_database[id]

@app.patch("/todos/{id}", status_code=200)
async def update_todo_by_id(id: int, request: Request):
    new_todo = await request.json()
    for todo in fake_database:
        if (todo["id"]==id):
            updated_todo=todo.update(new_todo)
    return updated_todo
    

@app.delete("/todos/{id}", status_code=200)
async def delete_todo_by_id(id: int):
    for todo in fake_database:
        if (todo["id"] == id):
            fake_database.remove(todo)
    raise HTTPException (status_code=404, detail= "Not Found")

  


