from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .models import Neighborhood,Business,Profile
from .email import send_welcome_email
from . forms import ProfileForm,BusinessForm
from django.db import transaction


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
	title = 'hood'
	name = Profile.objects.all()
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

@transaction.atomic
def create_profile(request):
    current_user = request.user 
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect( index )
    else:
        form = ProfileForm()
    return render(request,'profile.html',{"form":form,})

def business(request):
    user = request.user
    profile = Profile.find_profile_by_id(user)
    neighborhood = Neighborhood.objects.all()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_business = form.save(commit = False)
            new_business.user_id =  user
            new_business.neighborhood_id = neighborhood
            new_business.save()
            return redirect( index ) 
    else:
        form = BusinessForm()
    return render(request,'formbusiness.html',{"form":form})




def view_business(request):
   user = request.user
   profile = Profile.find_profile_by_id(user)
   # neighborhood = Neighborhood.find_neighborhood(profile.neighborhood_id.id)
   # businesses = Business.all_business()
   return render(request,'business.html',{"user":user,"profile":profile,})
