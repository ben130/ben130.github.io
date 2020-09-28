from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'recommend/home.html')
    #return HttpResponse('<h1>stay </h1>')

def savedplaylists(request):
    return render(request, 'recommend/savedPlaylists.html')

