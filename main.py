import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, url_for, session, redirect

app = Flask(__name__)
app.config['SESSION_COOKIE_NAME'] = 'Cookie'
app.secret_key = 'SECRET_KEY'
TOKEN_INFO = 'token_info'

# Route for login handling
@app.route('/')
def login():
    '''
    Login generates authorization url, then redirects user to external url value.
    '''
    auth_url = create_spotify_oauth().get_authorize_url()
    return redirect(auth_url)

# Route for redirect URI after authorization
@app.route('/redirect')
def redirect_path():
    '''
    Redirect Path method exchanges Auth code to an access token and refresh token.
    '''
    session.clear()
    code = request.args.get('code')
    token_info = create_spotify_oauth().get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for('save_discover_weekly',_external=True))

# Route to save Weekly songs to Saved Weekly playlist
@app.route('/saveDiscoverWeekly')
def save_discover_weekly():
    '''
    Creates a "Saved Weekly" playlist, if it exists, method prepopulates a Saved Weekly playlist using items from Discover Weekly playlist ID
    '''
    try: 
        token_info = get_token()
    except:
        print('User not logged in')
        return redirect("/")

    sp = spotipy.Spotify(auth=token_info['access_token'])
    userID = sp.current_user()['id']
    
    current_playlist = sp.current_user_playlists()['items']
    saved_weekly_id = None
    discover_weekly_id = None
    
    for playlist in current_playlist:
        if(playlist['name'] == "Discover Weekly"):
            discover_weekly_id = playlist['id']
        if(playlist['name'] == "Saved Weekly"):
            saved_weekly_id = playlist['id']
    
    if not discover_weekly_id:
        return "Discover Weekly playlist not found"
    
    if not saved_weekly_id:
        saved_playlist = sp.user_playlist_create(userID, 'Saved Weekly', True)
        saved_weekly_id = saved_playlist['id']
    
    discover_playlist = sp.playlist_items(discover_weekly_id)
    song_uris = []
    for song in discover_playlist['items']:
        song_uri = song['track']['uri']
        song_uris.append(song_uri)
    sp.user_playlist_add_tracks(userID, saved_weekly_id, song_uris)
    
    return ('Discover Weekly songs added successfully')

# Auxiliary functions
def get_token():
    '''
    Retrieves token from session, and maintains a refresh token when expired
    '''
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login', _external=False))
    
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if(is_expired):
        spotify_oauth = create_spotify_oauth()
        token_info = spotify_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info

def create_spotify_oauth():
    '''
    Calls Spotify OAuth
    '''
    return SpotifyOAuth(
        client_id = "YOUR_CLIENT_ID",
        client_secret = "YOUR_CLIENT_SECRET",
        redirect_uri = url_for('redirect_path', _external=True),
        scope='user-library-read playlist-modify-public playlist-modify-private'
    )

app.run(debug=True)