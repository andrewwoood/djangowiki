from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def loadEntry(request, entryTitle):
    if util.get_entry(entryTitle) == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "entryTitle" : entryTitle.capitalize() ,
            "entryData" : markdown(util.get_entry(entryTitle))
        })

# def greet(request, name):
#     return render(request, "encyclopedia/entry.html",{
#         "entryTitle" : name.capitalize() ,
#         "entryData" : util.get_entry(name)

#     })
