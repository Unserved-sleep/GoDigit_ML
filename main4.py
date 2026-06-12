from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# 1. Basic route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

# 2. Request object example
@app.get("/request-info")
async def request_info(request: Request):
    return {
        "client_host": request.client.host,
        "url": str(request.url),
        "method": request.method
    }

# 3. Custom response example
@app.get("/custom-response")
def custom_response():
    data = {"status": "success", "message": "Custom response returned"}
    return JSONResponse(content=data, status_code=200)

# 4. Path parameter routing
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# 5. Query parameter routing
@app.get("/search")
def search(query: str):
    return {"searched_query": query}

# 6. Serialization example
@app.get("/student")
def get_student():
    student = {
        "name": "Anita",
        "age": 20,
        "department": "IT"
    }
    return student

# 7. De-serialization example
class Student(BaseModel):
    name: str
    age: int
    department: str

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "received_data": student
    }