from fastapi import FastAPI
from pydantic import BaseModel
from ResearchAgent import run_agent

app = FastAPI()

class Request(BaseModel):
    query: str

@app.post("/research")
def research(request: Request):
    result = run_agent(request.query)
    return {"response": result}