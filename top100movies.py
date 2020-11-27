import requests
from bs4 import BeautifulSoup

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url)
website = response.text

soup = BeautifulSoup(website, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_titles]
movie = movie_titles[::-1]

with open("movis.text", mode="w") as file:
	for i in movie:
		file.write(f"{i}\n")