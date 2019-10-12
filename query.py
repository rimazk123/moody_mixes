import spotipy
import spotipy.util as util
import spotipy.oauth2 as oauth2
import json

credentials = oauth2.SpotifyClientCredentials(
        client_id='15e7265b21d14a6eadbff697e2d4fa6b',
        client_secret='f6d462e641f1424f973eb80e01c9d46b')

token = credentials.get_access_token()
spotify = spotipy.Spotify(auth=token)


def get_playlist(searchQuery):
    results = spotify.search(q=searchQuery, type='playlist', limit=1)

    return results['playlists']['items'][0]['external_urls']['spotify']

