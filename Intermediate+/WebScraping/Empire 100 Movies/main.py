import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title_tags = soup.select(selector="h3.title")

titles = [title.text for title in title_tags[::-1]]

with open ("movies.txt", "w") as output_file:
    for title in titles:
        output_file.write(f"{title}\n")
