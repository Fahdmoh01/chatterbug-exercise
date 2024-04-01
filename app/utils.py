from pathlib import Path

import random

from fastapi import HTTPException, status
from app.schemas import PasswordFields as PasswordSchema


def password_generator(fields: PasswordSchema) -> str:
    """
    Generates passwords based on field options provided
    """
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()
    digits = "0123456789"
    symbols = "!@#$%^&*()-_=+[]{};':\",./<>?"

    password = ""
    if fields.lowercase:
        password += lowercase
    if fields.uppercase:
        password += uppercase
    if fields.digits:
        password += digits
    if fields.symbols:
        password += symbols

    if not password:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail={
                "error": "One of (lowercase, uppercase, digits, or symbols) must be set to True"
            },
        )
    return "".join(random.choice(password) for _ in range(fields.length))


def transform_data(movies_result):
    """
    Transforms data into a new format with only required information for presentation
    """
    movie_list = []
    for data in movies_result["results"]:
        movie_id = data["id"]
        movie_title = data["title"]
        movie_overview = data["overview"]
        movie_ratings = data["vote_average"]
        movie_release_date = data["release_date"]
        movie_poplarity = data["popularity"]
        movie_poster = data["poster_path"]
        movie_element = {
            "moive_id": movie_id,
            "movie_title": movie_title,
            "movie_poster": movie_poster,
            "movie_overview": movie_overview,
            "movie_ratings": movie_ratings,
            "movie_release_date": movie_release_date,
            "movie_poplarity": movie_poplarity,
        }
        movie_list.append(movie_element)
    return movie_list
