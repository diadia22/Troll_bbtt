from django.shortcuts import render
from main.models import Match_Info,Summoner_Info,League_Entries,Champion_Image,Item_Image,Main_Perk_Image,Sub_Perk_Image
from django.urls import reverse


# Create your views here.
def index(request):
    match_info=Match_Info.objects.all()
    # summoner_info = Summoner_Info.objects.get(summonerName='아이디가문제')
    # summoner_rank = League_Entries.objects.get(summonerName='아이디가문제')
    champion_image = Champion_Image.objects.all()
    item_image = Item_Image.objects.all()
    main_Perk_image = Main_Perk_Image.objects.all()
    sub_Perk_image = Sub_Perk_Image.objects.all()
    return render(request, 'search/search.html',
                   {
                #  'summoner_info':summoner_info, 
                #    'summoner_rank': summoner_rank, 
                   'champion_image': champion_image, 
                   'item_image':item_image, 
                   'main_Perk_image':main_Perk_image,
                   'sub_Perk_image':sub_Perk_image,
                   'match_info':match_info
                   })

def search(request,nickname):

    summoner_info = Summoner_Info.objects.get(summonerName=nickname)

    return render(request, 'search/search.html',{'summoner_info':summoner_info})

def ai(request, summonerName):
    pass
    # search/models.py -> database 구축(columns, 자료형(type)) 지정하는 Class 만들어주기
    # search/views.py -> database csv 넣어주는 식 하나 만들어주기(AWS hosting 되면 딱 한 번만 실행할 것)
    # api요청에 요청을 통해 받은 최종적인 dataframe을 database추가해주는데 중복(database에 있는 id를 검색한거라면 = if puuid 같을 때)되면 최신걸로 업데이트
