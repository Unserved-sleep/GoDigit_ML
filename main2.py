from fastapi import FastAPI
from fastapi.responses import JSONResponse

#custom response

app = FastAPI()

@app.get("/custom-response")
def custom_response():
    data = {"message": "This is a custom response"}
    return JSONResponse(content=data, status_code=201)

@app.get("/json-example")
def json_example():
    return {
        "name": "FastAPI",
        "version": 1.0,
        "features": ["fast", "simple", "modern"]
    }