import json
import pathlib
from typing import List, Union
from fastapi import FastAPI, Response
from models import Track

# instantiate the FastAPI app
app =FastAPI()

# create container for our data - to be loaded at app startup.
data = []

# define app start-up event
@app.on_event("startup")
async def startup_event():
    datapath = pathlib.Path() / 'data' / 'tracks.json'
    with open(datapath, 'r') as f:
        tracks = json.load(f)
        for track in tracks:
            data.append(Track(**track).dict())
    

@app.get('/tracks/', response_model=List[Track])
def tracks():
    return data

@app.get('/tracks/{track_id}/', response_model=Union[Track, str])
def track(track_id: int, response: Response):
    track = None
    for t in data:
        if t['id'] == track_id:
            track = t
            break
    if track is None:
        response.status_code = 404
        return "Track Not Found"
    return track

@app.post('/tracks/', response_model=Track, status_code=201)
def create_track(track:Track):
    track_dict=track_dict()
    track_dict['id']= max(data, lambda x: x['id']).get(id) + 1
    data.append(track_dict)
    return track_dict


@app.put('/tracks/{track_id}/', response_model=Union[Track, str])
def track(track_id: int,updated_track: Track, response: Response):
    track = None
    for t in data:
        if t['id'] == track_id:
            track = t
            break
    if track is None:
        response.status_code = 404
        return "Track Not Found"
    
    for key, val in updated_track.dict().items():
        if key!= 'id':
            track[key] = val
    return track


@app.delete('/tracks/{track_id}/')
def track(track_id: int, response: Response):
    track_index = None
    for idx, t in enumerate(data):
        if t['id'] == track_id:
            track_index = idx
            break
    if track_index is None:
        response.status_code = 404
        return "Track Not Found"
    

    del data(track_index)
    return Response(status_code=200)