#basic routing

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def home():
    return {"page": "home"}

@app.get("/about")
def about():
    return {"page": "about"}

@app.get("/contact")
def contact():
    return {"page": "contact"}

#with parameters
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
def search(query: str):
    return {"searched_for": query}

# serialization
@app.get("/serialize")
def serialize_data():
    student = {
        "name": "Ravi",
        "age": 21,
        "department": "CSE"
    }
    return student


#de-serialization
class Student(BaseModel):
    name: str
    age: int
    department: str

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student received successfully",
        "student_data": student
    }