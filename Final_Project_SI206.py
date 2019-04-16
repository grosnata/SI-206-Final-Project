# SI 206
# Final Project
# Jamie Neumann and Natalie Gross

import unittest
import requests
import json
import sqlite3
import urllib.request, urllib.parse, urllib.error
import sys
import spotipy
import spotipy.util as util
import spotify_info
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from youtube_api import YouTubeDataAPI

'''
client_id2 = spotify_info.SPOTIPY_CLIENT_ID
client_secret2 = spotify_info.SPOTIPY_CLIENT_SECRET
redirect_uri2 = spotify_info.SPOTIPY_REDIRECT_URI
spotify = spotipy.Spotify()
username = "neumann.jamiel@gmail.com"
scope = 'user-library-read'
token = util.prompt_for_user_token(username,scope,client_id=client_id2,client_secret=client_secret2,redirect_uri=redirect_uri2)
spotify = spotipy.Spotify(auth = token)
 

def get_ariana_songs():
    ariana_uri = 'spotify:artist:66CXWjxzNUsdJxJ2JdwvnR'
    results = spotify.artist_top_tracks(ariana_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_ladygaga_songs():
    lg_uri = 'spotify:artist:1HY2Jd0NmPuamShAr6KMms'
    results = spotify.artist_top_tracks(lg_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_pink_songs():
    pink_uri = 'spotify:artist:1KCSPY1glIKgitqW2TotWuXOR'
    results = spotify.artist_top_tracks(pink_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_taylorswift_songs():
    ts_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'
    results = spotify.artist_top_tracks(ts_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_beyonce_songs():
    beyonce_uri = 'spotify:artist:6vWDO969PvNqNYHIOW5v0m'
    results = spotify.artist_top_tracks(beyonce_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_drake_songs():
    drake_uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'
    results = spotify.artist_top_tracks(drake_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_brunomars_songs():
    bm_uri = 'spotify:artist:0du5cEVh5yTK9QJze8zA0C'
    results = spotify.artist_top_tracks(bm_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_eminem_songs():
    eminem_uri = 'spotify:artist:7dGJo4pcD2V6oG8kP0tJRR'
    results = spotify.artist_top_tracks(eminem_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_edsheeran_songs():
    es_uri = 'spotify:artist:6eUKZXaKkcviH0Ku9w2n3V'
    results = spotify.artist_top_tracks(es_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst

def get_justinbeiber_songs():
    jb_uri = 'spotify:artist:1uNFoZAHBGtllmzznpCI3s'
    results = spotify.artist_top_tracks(jb_uri)
    pop_lst = []
    for track in results['tracks'][:11]:
        title = track["name"]
        popularity = track["popularity"]
        pop_lst.append((title,popularity))
    return pop_lst


def setUpSongTable(ariana_tuples, lg_tuples, pink_tuples, ts_tuples, beyonce_tuples, drake_tuples, bm_tuples, eminem_tuples, es_tuples, jb_tuples, conn, cur):
    cur.execute('DROP TABLE IF EXISTS popularities')
    cur.execute('CREATE TABLE popularities(Ariana_Grande TEXT, Lady_Gaga TEXT, Pink TEXT, Taylor_Swift TEXT, Beyonce TEXT, Drake TEXT, Bruno_Mars TEXT, Eminem TEXT, Ed_Sheeran TEXT, Justin_Beiber TEXT)')
    ariana = []
    lg = []
    pink = []
    ts = []
    beyonce = []
    drake = []
    bm = []
    eminem = []
    es = []
    jb = []
    for song in  ariana_tuples:
        ariana.append(str(song[1]))
    for song in  lg_tuples:
        lg.append(str(song[1]))
    for song in  pink_tuples:
        pink.append(str(song[1]))
    for song in  ts_tuples:
        ts.append(str(song[1]))
    for song in  beyonce_tuples:
        beyonce.append(str(song[1]))
    for song in  drake_tuples:
        drake.append(str(song[1]))
    for song in  bm_tuples:
        bm.append(str(song[1]))
    for song in  eminem_tuples:
        eminem.append(str(song[1]))
    for song in  es_tuples:
        es.append(str(song[1]))
    for song in  jb_tuples:
        jb.append(str(song[1]))
    i = 0
    for i in range(10):
            _popularity_ariana = ariana[i]
            _popularity_lg = lg[i]
            _popularity_pink = pink[i]
            _popularity_ts = ts[i]
            _popularity_beyonce = beyonce[i]
            _popularity_drake = drake[i]
            _popularity_bm = bm[i]
            _popularity_eminem = eminem[i]
            _popularity_es = es[i]
            _popularity_jb = jb[i]
            cur.execute('INSERT INTO popularities (Ariana_Grande, Lady_Gaga, Pink, Taylor_Swift, Beyonce, Drake, Bruno_Mars, Eminem, Ed_Sheeran, Justin_Beiber) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            ,(_popularity_ariana,_popularity_lg,_popularity_pink,_popularity_ts,_popularity_beyonce,_popularity_drake,_popularity_bm,_popularity_eminem,_popularity_es,_popularity_jb))
            i += 1
    conn.commit()

def get_averages(lst):
    total = 0
    for elem in lst:
        total += int(elem)
    average = total/len(lst)
    return(average)

def barchart_averages():
    cur.execute("SELECT * FROM popularities")
    ariana = []
    lg = []
    pink = []
    ts = []
    beyonce = []
    drake = []
    bm = []
    eminem = []
    es = []
    jb = []
    for row in cur:
        ariana.append(int(row[0]))
        lg.append(int(row[1]))
        pink.append(int(row[2]))
        ts.append(int(row[3]))
        beyonce.append(int(row[4]))
        drake.append(int(row[5]))
        bm.append(int(row[6]))
        eminem.append(int(row[7]))
        es.append(int(row[8]))
        jb.append(int(row[9]))
    ariana_average = get_averages(ariana)
    lg_average = get_averages(lg)
    pink_average = get_averages(pink)
    ts_average = get_averages(ts)
    beyonce_average = get_averages(beyonce)
    drake_average = get_averages(drake)
    bm_average = get_averages(bm)
    eminem_average = get_averages(eminem)
    es_average = get_averages(es)
    jb_average = get_averages(jb)
    labels = ["Ariana Grande", "Lady Gaga", "Pink", "Taylor Swift", "Beyonce", "Drake", "Bruno Mars", "Eminem", "Ed Sheeran", "Justin Beiber"]
    counts = [ariana_average,lg_average,pink_average,ts_average,beyonce_average,drake_average,bm_average,eminem_average,es_average,jb_average]
    plt.bar(labels, counts, align = "center", color = ["lavenderblush", "pink", "lightpink", "hotpink", "deeppink", "navy", "blue", "dodgerblue", "deepskyblue", "skyblue"])
    plt.title("Comparison of Average Popularities for Songs of Recent Artists")
    plt.ylabel("Average Song Popularity (on a scale of 0 to 100)")
    plt.xlabel("Artist Name")
    plt.savefig("artist_popularity.png")
    plt.show()
'''

youtube_api = "AIzaSyALtuOrfBRq3Sc58WbHITyZFA2at153JbE"
yt = YouTubeDataAPI(youtube_api)
def get_youtube_data():
    results = yt.search("one kiss music video")
    print(results[0])

if __name__ == "__main__":
    '''
    ariana_tuples = get_ariana_songs()
    lg_tuples = get_ladygaga_songs()
    pink_tuples = get_pink_songs()
    ts_tuples = get_taylorswift_songs()
    beyonce_tuples = get_beyonce_songs()
    drake_tuples = get_drake_songs()
    bm_tuples = get_brunomars_songs()
    eminem_tuples = get_eminem_songs()
    es_tuples = get_edsheeran_songs()
    jb_tuples = get_justinbeiber_songs()
    conn = sqlite3.connect('song_popularities.sqlite')
    cur = conn.cursor()
    setUpSongTable(ariana_tuples,lg_tuples, pink_tuples, ts_tuples, beyonce_tuples, drake_tuples, bm_tuples, eminem_tuples, es_tuples, jb_tuples, conn, cur)
    '''
    #barchart_averages()
    get_youtube_data()
