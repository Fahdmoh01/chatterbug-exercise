import os
from fastapi import FastAPI, Request, Response, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from utils import password_generator, transform_data
from schema import PasswordFields as PasswordSchema
from dotenv import load_dotenv
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).parent.parent.absolute()
app.mount(
    "/static",
    StaticFiles(directory=Path.joinpath(BASE_DIR, "static")),
    name="static",
)
templates = Jinja2Templates(directory=Path.joinpath(BASE_DIR, "templates"))

load_dotenv(Path.joinpath(BASE_DIR, ".env"))
movies_url = os.environ["MOVIES_URL"]
access_token = os.environ["ACCESS_TOKEN"]


@app.post("/generate-password", status_code=status.HTTP_201_CREATED)
async def generate_password(additionalFields: PasswordSchema):
    """
    Generates a password according to selected field options in additionalFields.
    """
    password = password_generator(additionalFields)
    return JSONResponse({"generatedPassword": password, "length": len(password)})


# @app.get("/third-party-api")
