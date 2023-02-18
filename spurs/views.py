from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from rest_framework.generics import ListAPIView
from .models import match
from .serial import MatchSerializer



class MatchDetailView(ListAPIView):
    queryset = match.objects.all()
    serializer_class = MatchSerializer



# def matches(request):
#     myMatches = match.objects.all().values()
#     template = loader.get_template('temp.html')
#     context ={
#         "myMatches": myMatches,
#     }

#     return HttpResponse(template.render(context,request))










