import pandas as pd
import numpy as np
import requests 
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("TMDB_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the TMDB_API_KEY environment variable.")
user_input = input("Enter a movie name: ")
url = "https://api.themoviedb.org/3/search/movie"
params = {
    "api_key": api_key,
    "query": user_input,   
    "language": "en-US",
    "page": 1
}
response = requests.get(url, params=params)
data= response.json()
print(data)