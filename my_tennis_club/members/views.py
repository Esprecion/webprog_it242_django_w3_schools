from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("<h2>When term 3 is more crazy than this</h2>")