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


class UserResponse(BaseModel):
    name:str
    age:int


@app.get("/user", response_model=UserResponse)
def get_user():
    return{
        "name" : "Mohit",
        "age" : 24,
        "password": 123456
    }

