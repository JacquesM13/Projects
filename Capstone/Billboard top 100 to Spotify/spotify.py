import requests
import webbrowser
import os
from bs4 import BeautifulSoup
import urllib
import base64
import pprint

CLIENT_ID = "N/A"
CLIENT_SECRET = "N/A"
REDIRECT_URI = "https://www.example.com/"
AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"

TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token"



#  --- GET CODE ---

header = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "scope": "playlist-modify-public playlist-modify-private user-read-private user-read-email",
    "redirect_uri": REDIRECT_URI,
}

# encoded_params = urllib.parse.urlencode(header)
# url = AUTH_ENDPOINT + "?" + encoded_params
# webbrowser.open(url)

# Above outputs following
code = ""
#  --- GET BEARER TOKEN ---

auth_str_bytes = f"{CLIENT_ID}:{CLIENT_SECRET}".encode("ascii")
auth_str_64 = base64.b64encode(auth_str_bytes).decode('utf-8')

token_header = {
    "Authorization": f"Basic {auth_str_64}",
    "Content-Type": "application/x-www-form-urlencoded",
}

token_body = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": REDIRECT_URI,
}

# response = requests.post(url= TOKEN_ENDPOINT, data= token_body, headers= token_header)
# print(response)
# access_token_response = response.json()
# pprint.pp(access_token_response)

# Above gives
output = {
    'access_token': '',
    'token_type': 'Bearer',
    'expires_in': 3600,
    'refresh_token': '',
    'scope': 'playlist-modify-private playlist-modify-public user-read-email '
    'user-read-private'
}

default_header = {
    'Authorization': f"Bearer {output['access_token']}",
}


#  --- GET USER ID ---

header = {
    'Authorization': f"Bearer {output['access_token']}",
}

# response = requests.get(url= "https://api.spotify.com/v1/me", headers= header)
# print(response.json())
#
# user_id = response.json()['id']

user_id = ""


#  --- CREATE PLAYLIST ---

create_playlist_headers = {
    'Authorization': f"Bearer {output['access_token']}",
    'Content-Type': 'application/json',
}

create_playlist_body = {
    "name": "Test3"
}

# response = requests.post(url= f"https://api.spotify.com/v1/users/{user_id}/playlists", headers= create_playlist_headers, json= create_playlist_body)
# print(response.text)

playlist_id = ""


# --- FIND SONG ---

endpoint = 'https://api.spotify.com/v1/search'

artist_name = "Lana Del Rey"
track_name = "Henry, come on"

another_song_dict = {'Drake': "I'm Upset", 'Cardi B, Bad Bunny & J Balvin': 'I Like It', 'Ella Mai': "Boo'd Up", 'Childish Gambino': 'This Is America', 'Kanye West': 'No Mistakes', 'Juice WRLD': 'All Girls Are The Same'}

for artist, song in another_song_dict.items():

    query = f'artist:{artist} track:{song} '

    params = {
        'q': query,
        'type': 'track',
        'limit': 1,
        'market': 'GB'
    }

    response = requests.get(url= f"{endpoint}", params= params, headers= default_header)
    print(response.json())

    # response = {'tracks': {'href': 'https://api.spotify.com/v1/search?offset=0&limit=1&query=artist%3ALana%20Del%20Rey%20track%3AHenry%2C%20come%20on%20&type=track&market=GB', 'limit': 1, 'next': None, 'offset': 0, 'previous': None, 'total': 1, 'items': [{'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/00FQb4jTyendYWaN8pK0wa'}, 'href': 'https://api.spotify.com/v1/artists/00FQb4jTyendYWaN8pK0wa', 'id': '00FQb4jTyendYWaN8pK0wa', 'name': 'Lana Del Rey', 'type': 'artist', 'uri': 'spotify:artist:00FQb4jTyendYWaN8pK0wa'}], 'external_urls': {'spotify': 'https://open.spotify.com/album/0oCEyDEDeBFKxbwEmE9f5e'}, 'href': 'https://api.spotify.com/v1/albums/0oCEyDEDeBFKxbwEmE9f5e', 'id': '0oCEyDEDeBFKxbwEmE9f5e', 'images': [{'height': 640, 'width': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b2734fb0b47e965f62951205cc5a'}, {'height': 300, 'width': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e024fb0b47e965f62951205cc5a'}, {'height': 64, 'width': 64, 'url': 'https://i.scdn.co/image/ab67616d000048514fb0b47e965f62951205cc5a'}], 'is_playable': True, 'name': 'Henry, come on', 'release_date': '2025-04-11', 'release_date_precision': 'day', 'total_tracks': 1, 'type': 'album', 'uri': 'spotify:album:0oCEyDEDeBFKxbwEmE9f5e'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/00FQb4jTyendYWaN8pK0wa'}, 'href': 'https://api.spotify.com/v1/artists/00FQb4jTyendYWaN8pK0wa', 'id': '00FQb4jTyendYWaN8pK0wa', 'name': 'Lana Del Rey', 'type': 'artist', 'uri': 'spotify:artist:00FQb4jTyendYWaN8pK0wa'}], 'disc_number': 1, 'duration_ms': 311269, 'explicit': False, 'external_ids': {'isrc': 'GBUM72501764'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/6CYldrsUPBsiPtfLW4xZCl'}, 'href': 'https://api.spotify.com/v1/tracks/6CYldrsUPBsiPtfLW4xZCl', 'id': '6CYldrsUPBsiPtfLW4xZCl', 'is_local': False, 'is_playable': True, 'name': 'Henry, come on', 'popularity': 83, 'preview_url': None, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:6CYldrsUPBsiPtfLW4xZCl'}]}}

    uri = response.json()['tracks']['items'][0]['uri']


    # --- ADD SONGS TO PLAYLIST ---

    body = {
        "uris": [uri]
    }

    response = requests.post(url= f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks", json= body, headers= create_playlist_headers)
    print(response.text)
