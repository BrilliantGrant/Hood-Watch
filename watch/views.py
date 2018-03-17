from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .models import Neighbor,Business,Profile

# Create your views here.

@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'welcome.html')

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
