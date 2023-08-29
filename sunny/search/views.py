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
