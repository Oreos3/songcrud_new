#from django.shortcuts import render

# Create your views here.


###test
#from django.http import HttpResponse
 
 
#def index(request):
#  return HttpResponse("Hello Geeks")



from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from . models import Artiste
from . models import Song
