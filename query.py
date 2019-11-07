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
    # spotify = spotipy.Spotify(auth=token)
    global credentials
    global token
    global spotify
    
    try:
        results = spotify.search(q=searchQuery, type='playlist', limit=10)
    except spotipy.client.SpotifyException:
        # re-authenticate when token expires
        token = credentials.get_access_token()
        spotify = spotipy.Spotify(auth=token)
        
        # Get top 10 results
        results = spotify.search(q=searchQuery, type='playlist', limit=10)
        
    # Pick a result
    playlistIndex = random.randint(0, len(results['playlists']['items']) - 1)

    print(results['playlists']['items'][playlistIndex]['external_urls']['spotify'])

    return results['playlists']['items'][playlistIndex]['external_urls']['spotify']


