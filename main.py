from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def home():
    return{"message":"Hello,FastAPI!"}


@app.get("/student")
def hello():
    return{"message":"I am learning FastAPI"}


#users route
@app.get("/users")
def users():
    return{
        "users":["Mohit","Rohit","Amit"]

    }


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
