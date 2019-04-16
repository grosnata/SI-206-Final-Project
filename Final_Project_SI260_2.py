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
import pprint

'''

youtube_api = youtube_info.api_key
api_service_name = "youtube"
api_version = "v3"
yt = YouTubeDataAPI(youtube_api)

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = youtube_info.client_secret
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

youtube = build(api_service_name, api_version, developerKey = youtube_api) 

youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = youtube_api)

def get_youtube_data():
    #results = youtube.videos()
    results = youtube.search('videos', id='B7FJV9KIn58')
    print(results)
'''

youtube_api = youtube_info.api_key
yt = YouTubeDataAPI(youtube_api)
results = yt.search("Drake")
print(results)