from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ValidateRequest(BaseModel):
    token: str
    hwid: str


@app.post("/auth/validate")
def validate(request: ValidateRequest):
    return {}
