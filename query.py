import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import json
import random

credentials = oauth2.SpotifyClientCredentials(
        client_id='YOUR_ID_HERE',
        client_secret='YOUR_SECRET_HERE')

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)

'''
Returns a random playlist from set of 10, based on the search terms
'''
def get_playlist(searchQuery):
    results = spotify.search(q=searchQuery, type='playlist', limit=10)

    playlistIndex = random.randint(0, len(results['playlists']['items']) - 1)

    print(results['playlists']['items'][playlistIndex]['external_urls']['spotify'])

    return results['playlists']['items'][playlistIndex]['external_urls']['spotify']

