from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .models import Neighborhood,Business,Profile
from .email import send_welcome_email

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
	title = 'hood'
	name = Neighborhood.objects.all()
	return render(request, 'index.html',{"title":title,"name":name})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

def create_profile(request):
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( landing )
    else:
        form = ProfileForm()
    return render(request,'profile.html',{"form":form,})
