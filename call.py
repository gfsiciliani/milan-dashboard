# CALLING THE API - RapidAPI // Serie A

# general imports
import requests
import json
# import os # why is this commented out?

# import api key from text api_key.py
from api_key import rapidapi_API

# key call url
url = "https: //api-football-v1.p.rapidapi.com/v3/teams/statistics"

# Serie A ID
league_id = 135             # "Serie A - ITA"
# team IDs
team_id_male = 489          # AC Milan men
team_id_female = 1893       # AC Milan women
team_id_u19 = 15670         # AC Milan U19
team_id_ita_male = 76       # Italian national men
team_id_ita_female = 1748   # Italian national women


# define query
querystring = {"league":"135",
               "season":"2024",
               "team":"489"
}

headers = {
	"x-rapidapi-key": rapidapi_key  ,
	"x-rapidapi-host": "api-football-v1.p.rapidapi.com"
}

# CALL API
print(f'===== calling API =====')
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
