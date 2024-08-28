import requests
import json

body = {
      "name": "John Doe", 
      "message": "test", 
      "email":"bobby@didcoding.com"
}

body = json.dumps(body)



url = 'http://127.0.0.1:8000/'


res = requests.post(url+"contact/", body)

print(res.text)
