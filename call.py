# CALLING THE API - RapidAPI // Serie A

import requests
# from dotenv import load_dotenv, dotenv_values
import os

from api_key import rapidapi_key

print(rapidapi_key)

url = "https://serie-a2.p.rapidapi.com/leaderboard"

# load_dotenv()
# print(os.getenv("APIKEY"))

# headers = {
#        "X-RapidAPI-Key": apikey,
#        "X-RapidAPI-Host": "serie-a2.p.rapidapi.com"
#}

# print(f'===== calling API =====')
# response = requests.get(url, headers=headers)
# print(response.json())


league_id = 135             # "Serie A - ITA"

# team IDs
team_id_male = 489          # AC Milan men
team_id_female = 1893       # AC Milan women
team_id_u19 = 15670         # AC Milan U19
team_id_ita_male = 76       # Italian national men
team_id_ita_female = 1748   # Italian national women