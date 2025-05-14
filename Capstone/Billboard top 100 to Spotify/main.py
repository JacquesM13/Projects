import requests
from bs4 import BeautifulSoup
from spotify import Spotify

BILLBOARD_ENDPOINT = "https://www.billboard.com/charts/hot-100/"

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:137.0) Gecko/20100101 Firefox/137.0"}

date = input("What year do you want to travel to? (YYYY-MM-DD format): ")
# date = '2025-05-14'
response = requests.get(url= f"{BILLBOARD_ENDPOINT}{date}/", headers= header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select(selector= 'li.o-chart-results-list__item > h3#title-of-a-story')
artists = soup.select(selector= 'li.o-chart-results-list__item > h3#title-of-a-story + span.c-label')

song_list = [song.text.strip() for song in songs]
artist_list = [artist.text.strip().replace('Featuring', '') for artist in artists]

song_dict = dict(zip(artist_list, song_list))
# print(song_dict)

spotify = Spotify()

redirect = input("Paste URL here: ")
code = redirect.split('code=')[1]

spotify.get_bearer(code)
spotify.get_user_id()
playlist_name = input("What would you like to call your playlist? ")
spotify.create_playlist(playlist_name)
# artist, song = input("What song would you like to add to the playlist? (artist, song)? ").split(', ')
# print(artist)
# print(song)

for artist, song in song_dict.items():
    spotify.get_song(artist, song)
