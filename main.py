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
@app.get("/users/{user_id}")
def get_user(user_id:int):
    return{"user_id": user_id}



#query parameters
#/users?name=mohit
#/products?price=1000
@app.get("/users")
def get_users(name):
    return{"Name": name}

#optional parameter
@app.get("/users")
def get_users(name: str = None):
    return{"Name": name}

#default values
@app.get("/products")
def get_users(limit: int = 10):
    return{"limit": limit}

#
@app.get("/items")
def get_users(name:str=None,price:int=0):
    return{
        "name": name,
        "price":price
    }