import os
import requests
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, RedirectResponse

from utils import password_generator, transform_data  # comment out to run tests
from schema import PasswordFields as PasswordSchema  # comment out to run tests

# from .utils import password_generator, transform_data  # uncomment to run tests
# from .schema import PasswordFields as PasswordSchema  # uncomment to run tests
from dotenv import load_dotenv
from pathlib import Path

app = FastAPI()
BASE_DIR = Path(__file__).parent.parent.absolute()

# mounting staticfiles
app.mount(
    "/static",
    StaticFiles(directory=Path.joinpath(BASE_DIR, "static")),
    name="static",
)

# mounting templates
templates = Jinja2Templates(directory=Path.joinpath(BASE_DIR, "templates"))

# loading and setting environment variables
load_dotenv(Path.joinpath(BASE_DIR, ".env"))
MOVIES_URL = os.environ["MOVIES_URL"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]


# Routers
@app.get("/")
async def index():
    """Redirects user to Swagger(/docs endpoint)"""
    return RedirectResponse("/docs")


@app.post("/generate-password")
async def generate_password(additionalFields: PasswordSchema):
    """
    Generates a password based on the field options provided in additionalFields through the request payload.
    [method: POST]
    [params: length,symbols,digits,lowercase,uppercase]
    """
    password = password_generator(additionalFields)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"generated_password": password, "length": len(password)},
    )


@app.get("/third-party-api")
async def get_movies(request: Request):
    """
    Fetchs data from third-party api https://developer.themoviedb.org/reference/discover-movie
    and serves the transformed data to movies.html for presentation.
    [method: GET]
    [params: None]
    """
    try:
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }
        # fetched data in json format
        response = requests.get(MOVIES_URL, headers=headers)
        movies_result = response.json()

        # json data transformed to present only required information
        transformed_movie_data = transform_data(movies_result)

        return templates.TemplateResponse(
            "movies.html",
            {"request": request, "movie_info": transformed_movie_data[:10]},
        )
    except (ConnectionError, TimeoutError) as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": f"Error fetching data: {e}"},
        )
