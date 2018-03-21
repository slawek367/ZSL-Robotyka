import json
import requests
import sys

#We need to specify what data on what data we working
headers = {'Content-Type': 'application/json; charset=utf-8'}

# RUN GET REQUEST to URL
url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
response = requests.get(url, headers)
response_code = response.status_code
response_json = json.loads(response.content.decode('utf-8'))

print("Status code: " + str(response_code))
print("First element from json response: \n" + str(response_json[0]))
print(response_json[0]['city']['commune']['communeName'])

for station in response_json:
    print(station['city']['commune']['communeName'])
