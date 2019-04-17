# SI 206
# Final Project - iTunes
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
import os
import spotify_final
import urllib
import itunespy
from itunespy import result_item

def getsonglength(query, artist):
    try:
        if "(" in query:
            index = query.find("(")
            tracks = itunespy.search_track(query[:index])
            info = tracks[0].get_track_time_minutes()
            return info
        else:
            tracks = itunespy.search_track(query)
            info = tracks[0].get_track_time_minutes()
            return info
    except:
        print("There is an error, you need to retype the song name. Song name: " + query + " by " + artist)
        user = input("Retype song name:")
        tracks = itunespy.search_track(user)
        info = tracks[0].get_track_time_minutes()
        return info
        

def getAverage(lst):
    total = 0
    for elem in lst:
        total += float(elem)
    average = total / len(lst)
    return average

def setUplengthTable(ariana_final, lg_final, pink_final, ts_final, beyonce_final, drake_final, bm_final, eminem_final, es_final, jb_final, conn, cur):
    cur.execute('DROP TABLE IF EXISTS length')
    cur.execute('CREATE TABLE length(Ariana_Grande TEXT, Lady_Gaga TEXT, Pink TEXT, Taylor_Swift TEXT, Beyonce TEXT, Drake TEXT, Bruno_Mars TEXT, Eminem TEXT, Ed_Sheeran TEXT, Justin_Beiber TEXT)')
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
        ariana.append((getsonglength(song, "Ariana Grande")))
    for song in lg_final:
        lg.append((getsonglength(song, "Lady Gage")))
    for song in pink_final:
        pink.append((getsonglength(song, "Pink")))
    for song in ts_final:
        ts.append((getsonglength(song, "Taylor Swift")))
    for song in beyonce_final:
        beyonce.append((getsonglength(song, "Beyonce")))
    for song in drake_final:
        drake.append((getsonglength(song, "Drake")))
    for song in bm_final:
        bm.append((getsonglength(song, "Bruno Mars")))
    for song in eminem_final:
        eminem.append((getsonglength(song, "Eminem")))
    for song in es_final:
        es.append((getsonglength(song, "Ed Sheeran")))
    for song in jb_final:
        jb.append((getsonglength(song, "Justin Beiber")))
    i = 0
    for i in range(10):
        _length_ariana = ariana[i]
        _length_lg = lg[i]
        _length_pink = pink[i]
        _length_ts = ts[i]
        _length_beyonce = beyonce[i]
        _length_drake = drake[i]
        _length_bm = bm[i]
        _length_eminem = eminem[i]
        _length_es = es[i]
        _length_jb = jb[i]
        cur.execute('INSERT INTO length (Ariana_Grande, Lady_Gaga, Pink, Taylor_Swift, Beyonce, Drake, Bruno_Mars, Eminem, Ed_Sheeran, Justin_Beiber) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(_length_ariana,_length_lg,_length_pink,_length_ts,_length_beyonce,_length_drake,_length_bm,_length_eminem,_length_es,_length_jb))
        i += 1
    conn.commit()

def barchart_length():
    cur.execute("SELECT * FROM length")
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
        ariana.append(row[0])
        lg.append(row[1])
        pink.append(row[2])
        ts.append(row[3])
        beyonce.append(row[4])
        drake.append(row[5])
        bm.append(row[6])
        eminem.append(row[7])
        es.append(row[8])
        jb.append(row[9])
    ariana_length = getAverage(ariana)
    lg_length = getAverage(lg)
    pink_length = getAverage(pink)
    ts_length = getAverage(ts)
    beyonce_length = getAverage(beyonce)
    drake_length = getAverage(drake)
    bm_length = getAverage(bm)
    eminem_length = getAverage(eminem)
    es_length = getAverage(es)
    jb_length = getAverage(jb)
    labels = ["Ariana Grande", "Lady Gaga", "Pink", "Taylor Swift", "Beyonce", "Drake", "Bruno Mars", "Eminem", "Ed Sheeran", "Justin Beiber"]
    counts = [ariana_length,lg_length,pink_length,ts_length,beyonce_length,drake_length,bm_length,eminem_length,es_length,jb_length]
    plt.bar(labels, counts, align = "center", color = ["darkslategray", "teal", "darkturquoise", "cyan", "paleturquoise", "aquamarine", "mediumspringgreen", "mediumseagreen", "seagreen", "darkgreen"])
    plt.title("Average Song Length of Recent Artists' Top Ten Songs")
    plt.ylabel("Average Song Length(in minutes)")
    plt.xlabel("Artist Name")
    plt.savefig("artist_songlength.png")
    plt.show()
    return(("Ariana Grande", ariana_length), ("Lady Gaga", lg_length), ("Pink", pink_length), ("Taylor Swift", ts_length), ("Beyonce", beyonce_length), ("Drake", drake_length), ("Bruno Mars", bm_length), ("Eminem", eminem_length), ("Ed Sheeran", es_length), ("Justin Beiber", jb_length))

def getlst(lst):
    final_lst = []
    for elem in lst:
        final_lst.append(elem[0])
    return final_lst

if __name__ == "__main__":
    
    conn = sqlite3.connect('song_length.sqlite')
    cur = conn.cursor()

    ariana_lst = spotify_final.get_ariana_songs()
    ariana_final = getlst(ariana_lst)

    lg_lst = spotify_final.get_ladygaga_songs()
    lg_final = getlst(lg_lst)

    pink_lst = spotify_final.get_pink_songs()
    pink_final = getlst(pink_lst)

    ts_lst = spotify_final.get_taylorswift_songs()
    ts_final = getlst(ts_lst)

    beyonce_lst = spotify_final.get_beyonce_songs()
    beyonce_final = getlst(beyonce_lst)

    drake_lst = spotify_final.get_drake_songs()
    drake_final = getlst(drake_lst)

    bm_lst = spotify_final.get_brunomars_songs()
    bm_final = getlst(bm_lst)

    eminem_lst = spotify_final.get_eminem_songs()
    eminem_final = getlst(eminem_lst)

    es_lst = spotify_final.get_edsheeran_songs()
    es_final = getlst(es_lst)

    jb_lst = spotify_final.get_justinbeiber_songs()
    jb_final = getlst(jb_lst)
    
    setUplengthTable(ariana_final, lg_final, pink_final, ts_final, beyonce_final, drake_final, bm_final, eminem_final, es_final, jb_final, conn, cur)
    
    fl = open("lengthfile.txt", 'w')
    for elem in barchart_length():
        fl.write("Using the top 10 songs from the spotify information, we found the average song length for each artist.")
        fl.write("{} has an average length of {} on their top ten songs".format(elem[0], elem[1]))
        fl.write('\n')
    fl.close()
    
    
