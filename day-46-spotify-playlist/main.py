import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import ast

SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "http://example.com/"

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
top_100_songs = [song.getText() for song in all_songs]

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

with open("token.txt") as token_file:
    token_data = token_file.read()
    token_data = ast.literal_eval(token_data)
    access_token = token_data["access_token"]

# Searching Spotify for songs to get the URIs
song_uris = []
for song in top_100_songs:
    song_data = sp.search(f"track: {song} year: {date.split('-')[0]}", limit=1, type='track')
    try:
        song_uris.append(song_data['tracks']['items'][0]['uri'])
    except IndexError:
        pass
    continue

# Creating a new private playlist in Spotify
playlist_creation_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

playlist_params = {
    "name": f"{date} Billboard 100",
    "public": False,
    "description": f"Travel back in time by listening to these top 100 songs from {date}.",
}
# response = requests.post(url=playlist_creation_endpoint, json=playlist_params, headers=headers)

# Adding songs to the playlist
playlist_id = ""  # Hard coded based on the output of the post request above

add_tracks_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
add_tracks_params = {
    "uris": song_uris,
}

# response = requests.post(url=add_tracks_endpoint, json=add_tracks_params, headers=headers)
# print(response.text)
