from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def home():
    return{"message":"Hello,FastAPI!"}


@app.get("/student")
def hello():
    return{"message":"I am learning FastAPI"}



    


@app.get("/student")
def student():
    return{
         "name":"Mitali",
         "course": "BCA",
         "subject":"Python"
    }


@app.get("/profile")
def profile():
    return{
         "name":"Mitali",
         "course": "BCA",
         "subject":"Python"
    }

#dyanamic parameters
# @app.get("/users/{user_id}")
# def get_user(user_id:int):
    # return{"user_id": user_id}



#query parameters
#/users?name=mohit
#/products?price=1000
# @app.get("/consumers")
# def get_consumers(name):
    # return{"Name": name}

#optional parameter
# @app.get("/users")
# def get_users(name: str = None):
    # return{"Name": name}

#default values
# @app.get("/products")
# def get_users(limit: int = 10):
#     return{"limit": limit}

#
# @app.get("/items")
# def get_users(name:str=None,price:int=0):
#     return{
#         "name": name,
#         "price":price
    # }

# @app.post("/create_user")
# def create_user(user:dict):
#     return{
#         "message:user created",
#         "data  ;  user"
   

# from pydantic import BaseModel

# class user(BaseModel):
#       name: str
#       age : int

# @app.post("/create_user")
# def create_user(user:user):
#      return{
#          "message:user created",
#         "data  ;  user"
#      }


#pydantic model
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()


# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")
# def create_user(user:User):
#     return{
#         "message":"User Created",
#         "data": user

#     }

#nested models

# class Address(BaseModel):
#     city:str
#     pincode:int


# class User(BaseModel):
#     name:str
#     age: int
#     address:Address

# @app.post("/create_user")
# def create_user(user:User):
#     return user




# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()

# todos=[]
# class Todo(BaseModel):
#     id:int
#     title:str
#     completed:bool

# #create api

# @app.post("/todos")
# def create_todo(todo:Todo):
#     todos.append(todo)
#     return{"message":"TODO added","data":todo}



# @app.get("/todos")
# def get_todos():
#     return todos


# @app.get("/todos/{todo_id}")
# def get_todo(todo_id:int):
#     for todo in todos:
#         if todo.id == todo_id:
#             return todo
#     return{"error":"Todo not found"}

# @app.put("/todos/{todo_id}")
# def update_todo(todos_id:int,update_todo:Todo):
#     for index,todo in enumerate(todos):
#         if todo == todos_id:
#            todos[index]= update_todo
#            return{
#                  "message":"Data Updated",
#                  "data":update_todo
               
#            }

# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id:int):
#   for index,todo in enumerate(todos):  
#         if todo == todo_id:
#             todos.pop(index)
#             return{"message":"Data Deleted"}



from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# users=[]

# class User(BaseModel):
#     name:str
#     age:int
# @app.post("/users")
# def create_user(user:User):
#     users.append(user)
#     return{
#         "message": "User Created",
#          "data" : user
#     }

# @app.put("/users?{user_id}")
# def updated_user(user_id:int,user:User,notify:bool=False):
#     if user_id < len(users):
#         users[user_id]=user

#         return{

#             "message":"User Updated",
#             "notify": notify,
#             "data" : user
#         }
#     return{
#         "error": "User not found"
#     }


# class UserResponse(BaseModel):
#     name:str
#     age:int


# @app.get("/user", response_model=UserResponse)
# def get_user():
#     return{
#         "name" : "Mohit",
#         "age" : 24,
#         "password": 123456
#     }


# from fastapi import FastAPI,status,HTTPException
# app = FastAPI()

# @app.post("/create_user",status_code= status.HTTP_201_CREATED)
# def create_user():
#     return{
#         "message":"User Created"
#     }

# @app.get("/user")
# def get_user():
#     return{
#          "status": "Success",
    
#          "message": "User Fetched",
#          "data":{
#              "name": "Mohit",
#              "age": 24
#          }

#     }

# #error handling
# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail='User Not Found'
#         )
#     return{
#         "id": 1,
#         "name":"Mohit"
#     }



# from fastapi import FastAPI,HTTPException
# app= FastAPI()

# class UserNotFoundexception(Exception):
#      def __init_(self,name:str):
#          self.name=name

# @app.get("/user/{name}")
# def get_user(name:str):
#     if name != "mohit":
#         raise UserNotFoundexception(name)
#     return{
#         "name":name
#     }\

# @app.get("/user/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code=404,
#             detail="User Not Found"
#         )
#     return{
#         "id":1,
#         "name":"Mohit"
# )


from fastapi import FastAPI, Depends,Header,HTTPException
app=FastAPI()

# def common_logic():
#     return{
#          "message":"Commom Logic executed"
#     }
# @app.get("/home")
# def home(data = Depends (common_logic)):
#     return data


# def get_current_user():
#     return{
#        "user":"Mohit"
#     }

# @app.get("/profile")
# def profile(user=Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def profile(user=Depends(get_current_user)):
#     return user

# def varify_token(token:str = Header(None)):
#     if token != "mysecrettoken":
#         raise HTTPException(
#             status_code =401,
#             detail="unauthorized"
#         )
#     return{
#         "user" : "Authorized User"
    # }

# @app.get("/secure-data")
# def secure_data(user = Depends(varify_token)):
#     return{
#          "message" : "Secure data accessed",
#          "user": user
#     }

#MIDDLEWARE
from fastapi import FastAPI,Request
app= FastAPI()
# @app.middleware("http")
# async def log_middleware(request:Request,call_next):
#     start_time = time.time()

#     responce = await call_next(request)

#     process_time = time.time()-start_time

#     print(f"Path:{request.url.path}|Time:{process_time}")

#     return response



# @app.middleware("http")
# async def my_middleware(request:Request,call_next):
#     print("Request Recieved")

#     response = await call_next(request)

#     print("Response Sent")

#     return response


#=============================================================================================================================================
#sqlite
#=============================================================================================================================================
import sqlite3
from fastapi import FastAPI
app = FastAPI()
conn = sqlite3.connect("test.db",check_same_thread=False)
cursor = conn.cursor()
cursor=conn.cursor()
cursor.execute("""  
 CREATE TABLE IF NOT EXISTS todos(
         id INTEGER PRIMARY KEY,  title TEXT,
         completed TEXT
      )
  """)
conn.commit()

@app.get("/")
def home():
     return{
         "message": "SQLite Connected fine"
     }

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from fastapi import FastAPI, Depends

app=FastAPI()
Base = declarative_base()
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine (  
   DATABASE_URL,
   connect_args={"check_same_thread": False}

 )

sessionLocal = sessionmaker(bind=engine)

class Todo (Base):
    __tablename__  = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

Base.metadata.create_all(bind=engine)


# def get_db():
#   db = sessionLocal()
#   try:
#      yield db
#   finally:
#       db.close()

# @app.get("/")
# def home(db: Session = Depends (get_db)):
#     return{
#         "message":"DB connected fine"
#     }



Base.metadata.create_all(bind=engine)

#Dependency (DB session provide karega)
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todos")
def create_todo(title:str,db:Session = Depends(get_db)):
    todo = Todo(title=title,completed="False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
         "message":"Todo Created",
         "data": todo


    }

# #reas all data
# @app.get("/todos")
# def get_todos(db:Session =depends(get_db)):
#     todos = db.query(Todo).all()

#     return{
#         "Total": len(todos),
#         "data":todos
#     }


# @app.get("/todos/{todo_id}")
# def get_todo(todo_id=int,db:Session = Depends(get_db)):
#     todo = db.query(Todo).filter(Todo.id ==todo_id).first()

#     if not todo:
#         raise HTTPException(status_code=404,detail = "Todo not found")
#     return todo

# @app.put("/todos/{todo_id}")
# def update_todo(todo_id:int,tittle:str,db:Session=Depends(get_db)):
#     todo = db.query(Todo).filter(Todo.id == todo_id).first()

#     if not todo:
#             raise HTTPException(status_code=404,detail = "Todo not found")
#         return todo
#     todo.title=title
# db.commit()
# return{
#      "message":"Todo Updated  "  
#      "data" :todo
#      }

# #update
# @app.put("?todos/{todo_id}")
# def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
#     todo=db.query(Todo).filter(Todo.id == todo_id).first()

#     if not todo:
#         raise HTTPException(status_code=404,detail = "Todo not found")
#         return todo
#     db.delete(todo)
#     db.commit()

#     return{
#         "message":"Todo DELETED"
#     }
        
   