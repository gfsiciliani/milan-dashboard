# CALLING THE API - RapidAPI // Serie A

import requests
from dotenv import load_dotenv, dotenv_values
import os

url = "https://serie-a2.p.rapidapi.com/leaderboard"

load_dotenv()
print(os.getenv("APIKEY"))

# headers = {
#        "X-RapidAPI-Key": apikey,
#        "X-RapidAPI-Host": "serie-a2.p.rapidapi.com"
#}

print(f'===== calling API =====')
# response = requests.get(url, headers=headers)
# print(response.json())


