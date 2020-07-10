from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown
from django.shortcuts import redirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def load_entry(request, entryTitle):
    if util.get_entry(entryTitle) == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html", {
            "entryTitle" : entryTitle.capitalize() ,
            "entryData" : markdown(util.get_entry(entryTitle))
        })

def random_page(request):
    entries = util.list_entries()
    selectedPage = random.choice(entries)
    return redirect(f'/{selectedPage}')