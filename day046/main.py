import re

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy import SpotifyOAuth

billboard_hot_100_URL = "https://www.billboard.com/charts/hot-100"


def main():
    destination_date = ""

    while not re.compile(r"\d{4}-\d{2}-\d{2}").match(destination_date):
        destination_date = input("Which date do you want to travel to? Type it in this format: YYYY-MM-DD: ")

    create_day_top_100_playlist(destination_date, get_hot_100_list(destination_date))


def create_day_top_100_playlist(destination_date, songs):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-private"))

    # results = sp.search(q='track:layla artist:"derek & the dominos" year:1970', limit=1)
    playlist = sp.user_playlist_create(user="mr__cellophane", name=f"{destination_date}", public=False)
    # pprint(results)


def get_hot_100_list(destination_date):
    hot_100_request = requests.get(f"{billboard_hot_100_URL}/{destination_date}")
    hot_100_request.raise_for_status()

    soup = BeautifulSoup(hot_100_request.content, "html.parser")
    elements = soup.findAll(class_=re.compile("lrv-u-padding-l-1@mobile-max"))

    return [(normalize_element(element.find("span")), normalize_element(element.find("h3"))) for element in elements]


def normalize_element(song_element):
    return song_element.text.replace("\n", "").replace("\t", "")


if __name__ == "__main__":
    main()
