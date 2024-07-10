from fastapi import FastAPI
import uvicorn
from starlette.requests import Request

app = FastAPI()


@app.get("/")
async def ping_server():
    return {"message": "Hi From ollama"}




if __name__ == "__main__":
    uvicorn.run(app)
