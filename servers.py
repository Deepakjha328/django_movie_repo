import requests
import json


URL="http://127.0.0.1:8000/api/movie"

data = {
    'movie_name':'Bahubali',
    'description':' This is best movie i have watched.i will recomend to everyone to wath this movie',
    'released':'2011-04-25'
}

json_data = json.dumps(data)
r= requests.post(url=URL, data=json_data)
data= r.json()
print(data)