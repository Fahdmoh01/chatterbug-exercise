import os
import requests
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
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


@app.post("/generate-password")
async def generate_password(additionalFields: PasswordSchema):
    """Generates a password according to selected field options in additionalFields."""
    password = password_generator(additionalFields)
    return JSONResponse({"generatedPassword": password, "length": len(password)})


@app.get("/third-party-api")
async def get_movies(request: Request):
    """
    Movie data is fetched from third-party api https://developer.themoviedb.org/reference/discover-movie
    The data is transformed and served to movies.html for presentation.
    """
    try:
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        response = requests.get(movies_url, headers=headers)
        movies_result = response.json()

        # json data transformed to extracted need info
        transformed_movie_data = transform_data(movies_result)

        return templates.TemplateResponse(
            "movies.html",
            {"request": request, "movie_info": transformed_movie_data[:10]},
        )
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching data: {e}",
        )
