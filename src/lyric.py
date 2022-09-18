import requests

def get_lyrics_for_track(access_token, track_id):
    lyrics = []
    try:
        resp = requests.get(
            "https://spclient.wg.spotify.com/lyrics/v1/track/"+track_id,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer %s" % access_token
            }
        )
    except:
        raise ConnectionError

    if (resp.text and resp.json()):
      response = resp.json()
      lyrics = response.get("lines")
    else:
     raise AttributeError   
 
    return lyrics
