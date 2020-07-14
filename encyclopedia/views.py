from django.shortcuts import render
from django.http import HttpResponse
from markdown2 import markdown
from django.shortcuts import redirect
import random
from django.db.models import Q
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

class NewTaskForm(forms.Form):
    title = forms.CharField(label = "Title")
    content = forms.CharField(label = "Content", widget=forms.Textarea)

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

def newEntry(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        check = form.is_valid()
        title = form.cleaned_data["title"].capitalize()
        entries = util.list_entries()
        if form.is_valid() and not(title in entries):
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect(f'/{title}')
        else:
            return render(request, "encyclopedia/newEntry.html", {
                "form": form,
                "titleConflict" : True
            })
    else:
        return render(request, "encyclopedia/newEntry.html", {
            "form": NewTaskForm()
        })
 