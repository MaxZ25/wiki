from django.http import HttpResponse
from django.shortcuts import render
from . import util

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def getpage(request, name):
    if (util.get_entry(name) == None):
        return render(request, "hello/error.html")
    
    return render(request, "hello/entries.html", {
        "view_name": util.get_entry(name)
    })