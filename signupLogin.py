from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

app=FastAPI()

DATA_File="users.json"

class Register(BaseModel):
    phone : int
    email : str
    full_name: str
    password : str

class Login(BaseModel):
    phone : int
    password : str

def load_users():
    if not os.path.exists(DATA_File):
        with open(DATA_File, "w") as f:
            json.dump([], f)

    with open(DATA_File,"r") as f:
        return json.load(f)
    
def save_users(users):
    with open(DATA_File,"w") as f:
        return json.dump(users,f,indent=2)
    
@app.get("/")
def welcome_msg():
    return {"Welcome to form"}

@app.post("/register")
def Reg(user:Register):
    users=load_users()

    for i in users:
        if i["phone"]==user.phone:
            return{"message":"User Already Registered"}
        
    users.append(user.dict())
    save_users(users)
    return {"message": "Registered successfully", "user": user}

@app.post("/login")
def Log(data:Login):
    users=load_users()

    for u in users:
        if u["phone"]==data.phone:
            if u["password"]==data.password:
                return{"message":"login successfully"}
            else:
                return{"message":"incorrect password"}
    return {"message": "User not found, please register first"}


