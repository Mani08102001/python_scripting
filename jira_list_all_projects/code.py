import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://manikandanpari.atlassian.net/rest/api/3/project"

API_TOKEN = "enter your account api token"

auth = HTTPBasicAuth("manikandanpari2001@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output=json.loads(response.text)

for i in range(len(output)):
  print(output[i]["name"])

