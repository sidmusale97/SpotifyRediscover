import os
from flask import Flask, request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys


client_id = '719be6aedcdd4584af11be6ef76a45ab'
client_secret = 'aaf421fdd6924927a962d3c2309beed4'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                        client_secret=client_secret,
                                        redirect_uri="http://example.com"))

def create_app(test_config = None):
    
     # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/get-next-song')
    def getNextSong():
        ids = []
        limit = 50
        total = sp.current_user_saved_tracks()['total']

        for i in range(0,total, limit):
            batch = sp.current_user_saved_tracks(offset=i, limit=limit)['items']
            batch_ids = [item['track']['id'] for item in batch]
            ids += batch_ids
        
        intent = request.args.get('intent')
        c_id = request.args.get('c_id')
        if(intent == 'pos'):
            return 'pos'
        else:
            return 'neg'

    def parseTrackIds(tracks):
        ids = [track in tracks]
        
    
    return app
