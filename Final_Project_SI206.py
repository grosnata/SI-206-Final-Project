# SI 206
# Final Project
# Jamie Neumann and Natalie Gross

import unittest
import requests
import json
import urllib.request, urllib.parse, urllib.error
import sys
import spotipy
import spotipy.util as util
import spotify_info

client_id2 = spotify_info.SPOTIPY_CLIENT_ID
client_secret2 = spotify_info.SPOTIPY_CLIENT_SECRET
redirect_uri2 = spotify_info.SPOTIPY_REDIRECT_URI
spotify = spotipy.Spotify()
username = "neumann.jamiel@gmail.com"
scope = 'user-library-read'
token = util.prompt_for_user_token(username,scope,client_id=client_id2,client_secret=client_secret2,redirect_uri=redirect_uri2)
spotify = spotipy.Spotify(auth = token)


def get_drake_songs():
    drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
    results = spotify.artist_top_tracks(drake_uri)
    pop_lst = []
    i = 0
    for i in range(5):
        for track in results['tracks'][:11]:
            title = track["name"]
            popularity = track["popularity"]
            pop_lst.append((title,popularity))
        i += 1
    return pop_lst

def get_ariana_songs():
    ariana_uri = 'spotify:artist:66CXWjxzNUsdJxJ2JdwvnR'
    results = spotify.artist_top_tracks(ariana_uri)
    pop_lst = []
    i = 0
    for i in range(5):
        for track in results['tracks'][:11]:
            title = track["name"]
            popularity = track["popularity"]
            pop_lst.append((title,popularity))
        i += 1
    return pop_lst

if __name__ == "__main__":
    get_drake_songs()
    get_ariana_songs()
