import requests

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"new york","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Key": "eef7a3d5d8msh41169b01bd51a56p1255acjsn60b5ef5eee92",
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())