from fastapi import FastAPI, Request


#reading request data
app = FastAPI()

@app.get("/info")
async def get_info(request: Request):
    client_host = request.client.host
    url = str(request.url)
    headers = dict(request.headers)

    return {
        "client_host": client_host,
        "url": url,
        "headers": headers
    }