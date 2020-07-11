from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown
from django.shortcuts import redirect
import random
from django.db.models import Q

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

#when they search, i want to submit that info to the results page
#and then using that string, i loop over all entriese and check if search is a substring of entry
#if it is, then add to list of results. then list all entries in results
def search(request):
    if request.method == "GET":
        search_query = request.GET.get('search_box', None)
        entries = util.list_entries()
        results = []
        # For all entries, check if my search query is a substring. If it is, append it to results.  
        if search_query is not None:
            for entry in entries:
                if search_query.lower() in entry.lower():
                    results.append(entry)
            return render(request, "encyclopedia/results.html", {
                "results" : results
            })
        else:
            return render(request, "encyclopedia/results.html")
