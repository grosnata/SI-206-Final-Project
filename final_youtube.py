# SI 206
# Final Project - Youtube
# Jamie Neumann and Natalie Gross

import unittest
import requests
import json
import sqlite3
import urllib.request, urllib.parse, urllib.error
import sys
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from youtube_api import YouTubeDataAPI
import youtube_info
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.discovery import build
import spotify_final

youtube_api = youtube_info.api_key
api_service_name = "youtube"
api_version = "v3"
yt = YouTubeDataAPI(youtube_api)
client_secrets_file = youtube_info.client_secret


youtube_object = build(api_service_name, api_version, developerKey = youtube_api)

youtube_api = youtube_info.api_key
yt = YouTubeDataAPI(youtube_api)
results = yt.search("Drake")
video_id = results[0]['video_id']
'''
stuff = youtube_object.videos().list(id = video_id, part = "id, snippet, contentDetails, statistics").execute()
likes = stuff['items'][0]['statistics']['likeCount']
dislikes = stuff['items'][0]['statistics']['dislikeCount']
'''
def getnumbers(elem):
    results = yt.search(elem + "Music Video")
    video_id = results[0]['video_id']
    stuff = youtube_object.videos().list(id = video_id, part = "id, snippet, contentDetails, statistics").execute()
    likes = stuff['items'][0]['statistics']['likeCount']
    return likes

def addlikes(lst):
    total = 0
    for elem in lst:
        total += elem
    return total

def setUpLikesTable(ariana_final, lg_final, pink_final, ts_final, beyonce_final, drake_final, bm_final, eminem_final, es_final, jb_final, conn, cur):
    cur.execute('DROP TABLE IF EXISTS likes')
    cur.execute('CREATE TABLE like(Ariana_Grande TEXT, Lady_Gaga TEXT, Pink TEXT, Taylor_Swift TEXT, Beyonce TEXT, Drake TEXT, Bruno_Mars TEXT, Eminem TEXT, Ed_Sheeran TEXT, Justin_Beiber TEXT)')
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
    for song in ariana_final:
        ariana.append(str(getnumbers(song)))
    for song in lg_final:
        lg.append(str(getnumbers(song)))
    for song in pink_final:
        pink.append(str(getnumbers(song)))
    for song in ts_final:
        ts.append(str(getnumbers(song)))
    for song in beyonce_final:
        beyonce.append(str(getnumbers(song)))
    for song in drake_final:
        drake.append(str(getnumbers(song)))
    for song in bm_final:
        bm.append(str(getnumbers(song)))
    for song in eminem_final:
        eminem.append(str(getnumbers(song)))
    for song in es_final:
        es.append(str(getnumbers(song)))
    for song in jb_final:
        jb.append(str(getnumbers(song)))
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

def barchart_likes():
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
    ariana_likes = addlikes(ariana)
    lg_likes = addlikes(lg)
    pink_likes = addlikes(pink)
    ts_likes = addlikes(ts)
    beyonce_likes = addlikes(beyonce)
    drake_likes = addlikes(drake)
    bm_likes = addlikes(bm)
    eminem_likes = addlikes(eminem)
    es_likes = addlikes(es)
    jb_likes = addlikes(jb)
    labels = ["Ariana Grande", "Lady Gaga", "Pink", "Taylor Swift", "Beyonce", "Drake", "Bruno Mars", "Eminem", "Ed Sheeran", "Justin Beiber"]
    counts = [ariana_likes,lg_likes,pink_likes,ts_likes,beyonce_likes,drake_likes,bm_likes,eminem_likes,es_likes,jb_likes]
    plt.bar(labels, counts, align = "center", color = ["lavenderblush", "pink", "lightpink", "hotpink", "deeppink", "navy", "blue", "dodgerblue", "deepskyblue", "skyblue"])
    plt.title("Comparison of Number of Likes on Music Videos of Recent Artists")
    plt.ylabel("Numbers of Likes (added between top 10 songs)")
    plt.xlabel("Artist Name")
    plt.savefig("artist_lists.png")
    plt.show()
    return(("Ariana Grande", ariana_likes), ("Lady Gaga", lg_likes), ("Pink", pink_likes), ("Taylor Swift", ts_likes))
'''

results = yt.search("Music Video")
video_id = results[0]['video_id']
stuff = youtube_object.videos().list(id = video_id, part = "id, snippet, contentDetails, statistics").execute()
likes = stuff['items'][0]['statistics']['likeCount']
print(likes)
'''

if __name__ == "__main__":
    ariana_lst = spotify_final.get_ariana_songs()
    ariana_final = []
    for elem in ariana_lst:
        ariana_final.append(elem[0])
    ariana_likes = getnumbers(ariana_final)

    lg_lst = spotify_final.get_ladygaga_songs()
    lg_final = []
    for elem in lg_lst:
        lg_final.append(elem[0])
    lg_likes = getnumbers(lg_final)

    pink_lst = spotify_final.get_pink_songs()
    pink_final = []
    for elem in pink_lst:
        pink_final.append(elem[0])
    pink_likes = getnumbers(pink_final)

    ts_lst = spotify_final.get_taylorswift_songs()
    ts_final = []
    for elem in ts_lst:
        ts_final.append(elem[0])
    ts_likes = getnumbers(ts_final)

    beyonce_lst = spotify_final.get_beyonce_songs()
    beyonce_final = []
    for elem in beyonce_lst:
        beyonce_final.append(elem[0])
    beyonce_likes = getnumbers(beyonce_final)

    drake_lst = spotify_final.get_drake_songs()
    drake_final = []
    for elem in drake_lst:
        drake_final.append(elem[0])
    drake_likes = getnumbers(drake_final)

    bm_lst = spotify_final.get_brunomars_songs()
    bm_final = []
    for elem in bm_lst:
        bm_final.append(elem[0])
    bm_likes = getnumbers(bm_final)

    eminem_lst = spotify_final.get_eminem_songs()
    eminem_final = []
    for elem in eminem_lst:
        eminem_final.append(elem[0])
    eminem_likes = getnumbers(eminem_final)

    es_lst = spotify_final.get_edsheeran_songs()
    es_final = []
    for elem in es_lst:
        es_final.append(elem[0])
    es_likes = getnumbers(es_final)

    jb_lst = spotify_final.get_justinbeiber_songs()
    jb_final = []
    for elem in jb_lst:
        jb_final.append(elem[0])
    jb_likes = getnumbers(jb_final)
    conn = sqlite3.connect('song_likes.sqlite')
    cur = conn.cursor()
    setUpLikesTable(ariana_likes, lg_likes, pink_likes, ts_likes, beyonce_likes, drake_likes, bm_likes, eminem_likes, es_likes, jb_likes, conn, cur)
    #barchart_likes()
    fl = open("popularitiesfile.txt", 'w')
    for elem in barchart_likes():
        fl.write("{} has {} likes on their top 10 music videos combined".format(elem[0], elem[1]))
        fl.write('\n')
    fl.close()
