import os
import re

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth

billboard_hot_100_URL = "https://www.billboard.com/charts/hot-100"


def main():
    print("🎵 Welcome to the Musical Time Machine 🎵")

    if not required_env_is_set():
        exit(0)

    destination_date = ""
    date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")

    while not date_pattern.match(destination_date):
        destination_date = input("Which date 📅  do you want to travel to? (type it in this format: YYYY-MM-DD): ")

    hot_100_for_date = get_hot_100_list(destination_date)
    print(f"\nThe Hot 100 🔥 for {destination_date} were:")
    [print(f"{index + 1}. {artist} - {song}") for index, (artist, song) in enumerate(hot_100_for_date)]
    create_day_top_100_playlist(destination_date, hot_100_for_date)
    print("\nDone! ✅")


def create_day_top_100_playlist(destination_date, songs):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))
    playlist_name = f"{destination_date} Billboard 100"
    playlist = sp.user_playlist_create(user="mr__cellophane", name=playlist_name, public=False)
    queried_year = int(destination_date[:4])
    song_ids = []

    for artist, song in songs:
        search = sp.search(q=f'track:"{song}" artist:"{artist}" year:{queried_year - 1}-{queried_year}', limit=1)

        if len(search["tracks"]["items"]) > 0:
            song_ids.append(search["tracks"]["items"][0]["id"])

    print(f"\nSongs found on Spotify: {len(song_ids)}. Creating playlist '{playlist_name}'...")
    sp.playlist_add_items(playlist["id"], song_ids)


def get_hot_100_list(destination_date):
    hot_100_request = requests.get(f"{billboard_hot_100_URL}/{destination_date}")
    hot_100_request.raise_for_status()

    soup = BeautifulSoup(hot_100_request.content, "html.parser")
    elements = soup.findAll(class_=re.compile("lrv-u-padding-l-1@mobile-max"))

    return [(normalize_element(element.find("span")), normalize_element(element.find("h3"))) for element in elements]


def required_env_is_set():
    required_env_vars = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]

    for required_env_var in required_env_vars:
        if not os.getenv(required_env_var):
            print(f"Fatal: One or more required environment variables not set: {required_env_vars}")
            return False

    return True


def normalize_element(song_element):
    return song_element.text.replace("\n", "").replace("\t", "")


if __name__ == "__main__":
    main()
