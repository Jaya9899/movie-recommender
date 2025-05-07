import pandas as pd
import numpy as np
import requests 
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("TMDB_API_KEY")


# Function to get movie ID from name
def get_movie_id(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": title,
        "language": "en-US",
        "page": 1
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    if not data['results']:
        print("Movie not found.")
        return None
    
    # Return the first match
    movie = data['results'][0]
    print(f"Found: {movie['title']} (ID: {movie['id']})")
    return movie['id']


if not api_key:
    raise ValueError("API key not found. Please set the TMDB_API_KEY environment variable.")
user_input = input("Enter a movie name: ")
movie_id = get_movie_id(user_input)

def get_recommendation_titles(movie_id, count=5):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {
        "api_key": api_key,
        "language": "en-US",
        "page": 1
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if not data['results']:
        print("No recommendations found.")
        return []
    
    # Return the top `count` movie titles
    titles = [movie['title'] for movie in data['results'][:count]]
    return titles
print(f"Recommendations for {user_input}:",get_recommendation_titles(movie_id))