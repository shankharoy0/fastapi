# fastapi
implimenting 4 CRUD functions with fastapi

 The data was taken from git its a list of data which specifies number of tracks released by artists and their release date along with it

1) To begin with this first install uvicorn and fastapi using the code "pip install uvicorn fastapi"
2) Then get the dataset and write the "models.py" code
3) Then after writing the code for get you can write on the console of code editor "uvicorn main:app --reload" it will help to check if get is working properly.
4) write "https://localhost:8000/tracks/#number#" in the browser it will help you check if the track is available by id.
5) Then we can create a task and we can test it out by the command "curl -X POST -H "Content-Type: application/json" -d '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}' http://localhost:8000/tracks"
6) Then we can update the existing track and we can test it out by the command "curl -X PUT -H "Content-Type: application/json" -d '{"artist": "Sonic Youth", "title": "Silver Rocket", "last_play": "2017-10-18 15:15:26", "duration": 200}' http://localhost:8000/tracks/1"
7) Then we can delete an existing task and then test it out by the command "curl -X DELETE http://localhost:8000/tracks/1".
