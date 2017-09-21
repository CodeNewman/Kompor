from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from kompor.settings import BASE_DIR

def index(request):
    return HttpResponse("The service start successfully.")



