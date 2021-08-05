from bs4 import BeautifulSoup
import requests

URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"

response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="_h3_cuogz_1")

movies_list = [title.getText() for title in all_movies]
del movies_list[-1]
formatted_movies = [title.replace('\xa0', '') for title in movies_list]

with open("movies.txt", "w") as file:
    for movie in formatted_movies:
        file.write(f"{movie}\n")

# Scrape the data from Time Out and create a text file "movies.txt" with top 100 movies starting from 1.
