from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ValidateRequest(BaseModel):
    token: str
    hwid: str

class ValidateRequest2(BaseModel):
    license_key: str
    hwid: str

@app.post("/apii/auth/validate")
def validate(request: ValidateRequest):
    return {}

@app.post("/apii/auth/login")
def validate2(request: ValidateRequest2):
    return {}

