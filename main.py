#import module & packages
import requests
import json
import pandas as pd
from googleapiclient.discovery import build


URL = "https://www.googleapis.com/youtube/v3"
API_KEY = "AIzaSyAJWL9OthRwuuugdq7Dtl1cJcWKVhqmFRE"
ID_CHAINE = "UCUoUYZzge-StTmYj16TqxGA"

api_service_name = "youtube"
api_version = "v3"


# Get credentials and create an API client
youtube = build(
  api_service_name, api_version, developerKey=API_KEY)

request = youtube.channels().list(
  part="snippet,contentDetails,statistics",
  id=ID_CHAINE
)

response = request.execute()
print(response)