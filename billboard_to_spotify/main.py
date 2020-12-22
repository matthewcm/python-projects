from dotenv import load_dotenv

import os
import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

BILL = "https://www.billboard.com/charts/hot-100/"
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    redirect_uri="http://example.com",
    show_dialog=True
))

user_id = sp.current_user()["id"]


def scrape_top_tracks(url):
    print('Searching for top 100 songs...')

    response = requests.get(url)
    res_html = response.text
    soup = BeautifulSoup(res_html, "html.parser")
    all_songs = soup.find_all(name="span", class_="chart-element__information")

    songs = []

    for song in all_songs:
        name = song.findNext(name="span", class_="chart-element__information__song").getText()
        artist = song.findNext(name="span", class_="chart-element__information__artist").getText()
        songs.append((name, artist))

    return songs


def save_songs_to_file(songs):
    print('Saving songs to file...')

    with open("./songs.txt", mode="w") as file:
        for song in songs:
            file.write(f"{song}\n")


def search_spotify_for_tracks(songs):
    print('Finding spotify tracks...')

    song_uris = []
    for song in songs:
        try:
            song_id = sp.search(song)['tracks']['items'][0]['uri']
            song_uris.append(song_id)
        except IndexError:
            print(song[0] + ' ' + song[1] + ' Does not have spotify track')

    return song_uris


def create_spotify_playlist(date):
    print('Creating spotify playlist...')

    new_playlist = sp.user_playlist_create(user=user_id, name=date + " Billboard Top", public=False,
                                           description="Created with python")

    return new_playlist['id']


def add_tracks_to_playlist(playlist_id, tracks):
    print('Adding songs to playlist...')

    sp.playlist_add_items(playlist_id, tracks)


def prompt():
    print("Get the top 100 songs from specified date")
    print("Enter Date in format YYYY-MM-DD")
    date = input()

    songs = scrape_top_tracks(BILL + date)

    save_songs_to_file(songs)

    song_uris = search_spotify_for_tracks(songs)

    playlist_id = create_spotify_playlist(date)

    add_tracks_to_playlist(playlist_id, song_uris)


if __name__ == '__main__':
    prompt()
