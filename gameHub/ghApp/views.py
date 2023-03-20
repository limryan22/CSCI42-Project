from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse('Hello World! This came from the index view')

def getUserInfo(request, user_id):
    url = f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=YOUR_API_KEY&steamids={user_id}'