from sklearn.decomposition import TruncatedSVD
import pandas as pd
import requests
from api_key import api_key
from championData import champion

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

# print(input_summonerName('나쁜유저는없다').get('id'))

def input_summonerId(summonerId):#소환사 아이디로 마스터리 검색하고 검색해서 나온 숙련도 정보를 puuid 와 함께 csv 파일로 덮어써서 저장
    url = f"https://kr.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerId}"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
    }
    response = requests.get(url, headers=headers)
    print(response)
    df = pd.DataFrame(response.json())
    df = df[['puuid','championId','championLevel','championPoints']]
    exdf = pd.read_csv('riot_api/mastery.csv')
    concatenated_df = pd.concat([exdf, df])
    final_df = concatenated_df.drop_duplicates()
    # final_df.to_csv('riot_api/mastery.csv', index=False)
    return concatenated_df
print(input_summonerId('Db-vFaJ0iPKmgHo8eic9ZCpaeffCTwpdQAjuRmaC6TVyeA'))


# df = input_summonerId('Db-vFaJ0iPKmgHo8eic9ZCpaeffCTwpdQAjuRmaC6TVyeA')
# exdf = pd.read_csv('riot_api/mastery_2.csv')
# exdf = pd.DataFrame(exdf)
# exdf_dropped = exdf.drop(columns=['summonerName', 'championName'])
# exdf_dropped = pd.DataFrame(exdf_dropped)


# concat_df = pd.concat(exdf_dropped, df, ignore_index=True)
# concat_df.to_csv('riot_api/mastery_3.csv')