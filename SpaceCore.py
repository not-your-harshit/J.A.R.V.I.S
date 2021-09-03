import requests
import json

Api_key="4UY2GQvqDmZiIhj98wBoCltkBtVQyW3hR9NAsrkg"


def NasaNews():
 url = "https://api.nasa.gov/planetary/apod?api_key=" + (str(Api_key))
  

 
 params ={

    'date':Date,
    'hd':'True',
    'api_key': Api_key
 }

 response = requests.get(url, params)

 json_data = requests.get(url,params=params)
 json_data = json.loads(response.text)


 print (json_data)

if __name__ == '__main__':
 Date =('2021-08-10')
 NasaNews()

