import requests

def get_lyrics_for_track(access_token, track_id):
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

    response = resp.json()

    if (response.get("lines")):
       return response.get("lines")
    return 0
