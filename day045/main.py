import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

soup = BeautifulSoup(requests.get(URL).content, "html.parser")
raw_movie_list = soup.findAll(class_=re.compile("listicleItem_listicle-item__title__"))
sorted_movie_list = ['' for i in range(0, 100)]

for item in raw_movie_list:
    movie_title = " ".join(item.text.split(" ")[1:]).strip()
    movie_rank = int(item.text.split(" ")[0].replace(")", ""))
    sorted_movie_list[movie_rank - 1] = movie_title

with open("top_100_movies.txt", "w") as output_file:
    output_file.write("The best 100 movies are:\n")
    output_file.writelines([f"\n{rank + 1} - {movie}" for rank, movie in enumerate(sorted_movie_list)])
