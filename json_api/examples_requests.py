import json
import requests
import sys

#We need to specify on what data we are working
headers = {'Content-Type': 'application/json; charset=utf-8'}

# RUN GET REQUEST to URL
url = "http://api.gios.gov.pl/pjp-api/rest/station/findAll"
response = requests.get(url, headers)
response_code = response.status_code
response_json = json.loads(response.content.decode('utf-8'))

print("Status code: " + str(response_code))
print("First element from json response: \n" + str(response_json[0]))

