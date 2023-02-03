from fastapi import FastAPI, Request
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

@app.patch("/todos")
async def update_todo_by_id(fake_database, id, todo_request):
    for todo in fake_database:
        if todo["id"] == id:
            todo.update(todo_request)
            return todo
    return None


todo_request = jim
update_todo_by_id(fake_database, 0, jim)

#@app.delete('/todos')
#async def delete_todo_by_id(id: int):
 #   del fake_database
  #  return {'message': 'successfully deleted'}


#@app.patch("/todos")
#async def update_todo_by_id():
 #  return todo 

   
