import os

from fastapi import FastAPI, HTTPException, Cookie, Response
from dotenv import load_dotenv
from typing import Optional


load_dotenv()

app = FastAPI()

COOKIE_VALUE = os.getenv("COOKIE_VALUE") or "secret"


@app.get("/")
async def index():
    return {"message": "Cookies test"}


@app.post("/login")
async def login(response: Response):
    response.set_cookie(
        key="token",
        value=COOKIE_VALUE,
        httponly=True,
        samesite="lax",
        secure=True
    )
    
    return {"message": "Token setted!"}


@app.get("/data")
async def get_data(token: Optional[str] = Cookie(None)):
    if token is None or token != COOKIE_VALUE:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {"data": "Some data."}
