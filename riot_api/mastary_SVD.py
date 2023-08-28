from sklearn.decomposition import TruncatedSVD
import pandas as pd
import requests
from api_key import api_key

def input_summonerName(summonerName): # summonerName -> summonerId
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

print(input_summonerName('나쁜유저는없다'))