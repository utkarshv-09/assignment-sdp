from fastapi import FastAPI, HTTPException
import subprocess
import os
from pydantic import BaseModel
from chat import chatBot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class URLRequest(BaseModel):
    data: str

@app.post("/")
async def post_data(request: URLRequest):
    bot = chatBot(request.data)
    response = bot.chat_completion()
    return {"response": response}

@app.get("/version.json")
async def get_version():
    try:
        version = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode('utf-8')
        return {"version": version}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail="Could not retrieve version")

@app.get("/healthcheck")
async def healthcheck():
    if not os.getenv("GROQ_API_KEY"):
        raise HTTPException(status_code=500, detail="API key not defined")
    return {"status": "ok", "details": "All systems operational"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
