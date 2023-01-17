"""
TODO
"""

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

# CREATE ASGI (Asynchronous Server Gateway Interface)
app = FastAPI()

from api.routes import statements, quotes, profile

app.include_router(statements.router, prefix="/statements")
app.include_router(quotes.router, prefix="/quotes")
# app.include_router(profile.router, prefix="/profile")

@app.get("/")
async def root() -> JSONResponse:
    resp = { "Message" : "Welcome to my stock monetary! The path availables are - '/statements'."}
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp, media_type="application/json")

