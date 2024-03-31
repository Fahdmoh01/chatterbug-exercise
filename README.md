# Chatterbug-exercise
Coding exercise for the Junior Full Stack Developer position at Chatterbug Ltd.

# Description
This codebase allows a user to generate passwords based on password security best practices. It also allows the user to fetch the top 10
most popular movies using the TheMovieBD's API. Thus, this repository satisfies both the main objectives and optional objectives of the exercise repectively. I look forward to further discussing my suitability for the role in the interviews.

# Snapshots:
![](overall.gif)

# Usage
* Clone the repository
##
       git clone https://github.com/Fahdmoh01/chatterbug-exercise.git 

* Create a virtual environment
##
        python -m venv env

* Activate virtual environment
##
        source env/bin/activate

* Install dependencies from the requirements.txt
##
        pip install requirements.txt

* Generate Access Token and find the API URL  from TheMovieDB https://developer.themoviedb.org/reference/intro/authentication. For the purpose of evaluation, I will be providing my Access Token below and the API URL below:
##
        ACCESS_TOKEN = eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZTUzMGQ3ZGY3ZmFkNGYzMWY4M2Q0Y2M4NjM2NTIzNiIsInN1YiI6IjYwNWRmOTEyZjNlMGRmMDA3MzkxNDViMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.e8nwm4dk5HMerwzFSRoY6oLcaIEoy-jMOk2LNLpXZw0
##
        MOVIES_URL = https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc

* Run the command below to start the application. Ensure you are in the app directory
##
        uvicorn main:app --reload


# Using the /generate-password route.[Main Objective]
Routes can either be accessed on Postman, Swagger or any API tool of choice.
* Make a POST request to generate password
##
        POST http://127.0.0.1:8000/generate-password
        
        
* Example Request Payload to  /generate-password route:
##
        {
            "length": 12,
            "symbols": true,
            "digits": true,
            "lowercase": true,
            "uppercase": true
        }
* Response will be a password and the password length in JSON format. Example Response:
##
        {
            "generatedPassword": "H=OC3:;J]$F.",
            "length": 12
        }

# Using the /third-party-api route.[Optional Objective]
* Make a GET request to view the web page of the top 10 most popular movies in the world right now according to the ThemovieDB
##
        GET http://localhost:8000/third-party-api

* Response will be a webpage:
![](thirdparty.gif)

- Author: Fahd Mohammed 
- Email: fahdmoh.1@gmail.com