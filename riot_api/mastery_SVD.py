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

# print(input_summonerName('아이디가문제').get('id'))

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
    df = pd.DataFrame(response.json())
    df = df[['puuid','championId','championLevel','championPoints']]
    to_add_puuid = df.loc[0]['puuid']
    exdf = pd.read_csv('riot_api/mastery.csv')
    exdf = exdf[exdf['puuid'] != to_add_puuid] #새로 추가하는 data가 이미 있는 유저의 데이터라면 그 유저에 대한 기존 데이터 다 삭제
    final_df = pd.concat([exdf, df])
    final_df.to_csv('riot_api/mastery.csv', index=False)
    return final_df
# input_summonerId('5ypezW81tzdXWE5NwmHLoDBlZJXddWOnp9d2nN3BWc-dIns')


def point_ML(df): # 위에서 나온 dataframe으로 머신러닝 돌리는데 마지막에 추가된 puuid(소환사를 검색해주는 거임)
    df = df[['puuid', 'championId', 'championPoints']]
    duplicates = df.duplicated(subset=['puuid', 'championId'], keep=False)
    pivot_df = df.pivot(index='puuid', columns='championId', values='championPoints')
    fill_na_df = pivot_df.fillna(0)
    svd = TruncatedSVD(n_components=25) # 컴포넌트는 바꿔주면 됨(25가 적당했어서 25로함)
    df_point_transformed = svd.fit_transform(fill_na_df)
    df_point_transformed = pd.DataFrame(df_point_transformed, index=fill_na_df.index)
    df_point_predicted = svd.inverse_transform(df_point_transformed)
    df_point_predicted = pd.DataFrame(df_point_predicted, columns=fill_na_df.columns, index=fill_na_df.index)
    for champion in pivot_df.columns:
        for user in pivot_df.index:
            if pd.isnull(pivot_df.loc[user, champion]):
                fill_na_df.loc[user, champion] = df_point_predicted.loc[user, champion]
    recommendations = {}
    for user in fill_na_df.index:
        original_scores = pivot_df.loc[user]
        predicted_scores = fill_na_df.loc[user]
        
        # 원래 점수가 낮은 챔피언들 중에서 예측 점수가 높은 챔피언을 찾습니다.(3명만)
        low_original_high_predicted = predicted_scores[original_scores < original_scores.median()].nlargest(3)
        
        # 해당 사용자에 대한 추천을 저장합니다.
        recommendations[user] = low_original_high_predicted.index.tolist()

    # 추천 결과를 출력합니다.
    print(recommendations.get(df.iloc[-1]['puuid']))
# point_ML(df)

nickname = '아이디가문제'
point_ML(input_summonerId(input_summonerName('아이디가 문제').get('id')))


