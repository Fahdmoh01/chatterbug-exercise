# chatterbug-exercise
Coding exercise solution for Chatterbug Ltd

# description
This codebase allows a user to generate passwords. It also allows the user to fetch the top 10
most popular movies using the TheMovieBD's API.

# usage

* clone the repository
##
       git clone https://github.com/Fahdmoh01/chatterbug-exercise.git 

* create a virtual environment
##
        python -m venv env

* install depends from the requirements.txt
##
        pip install requirements.txt

* generate Access Token and find the API URL  from TheMovieDB https://developer.themoviedb.org/reference/intro/authentication. For the purpose of evaluation, I will be providing my Access Token below and the API URL below:
##
        ACCESS_TOKEN = eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZTUzMGQ3ZGY3ZmFkNGYzMWY4M2Q0Y2M4NjM2NTIzNiIsInN1YiI6IjYwNWRmOTEyZjNlMGRmMDA3MzkxNDViMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.e8nwm4dk5HMerwzFSRoY6oLcaIEoy-jMOk2LNLpXZw0
##
        MOVIES_URL =https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc

* run the command below to start the application. ensure you in the app directory
##
        uvicorn main:app --reload