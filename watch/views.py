from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .models import Neighborhood,Business,Profile,Post
from .email import send_welcome_email
from . forms import ProfileForm,BusinessForm,PostForm
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
    current_user = request.user
    current_profile = Profile.find_profile_by_id(current_user)
    current_neighborhood = Neighborhood.objects.all()

    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_business = form.save(commit = False)
            new_business.user_id =  current_user
            new_business.neighborhood = current_neighborhood
            new_business.save()
            return redirect( index ) 
    else:
        form = BusinessForm()
    return render(request,'business.html',{"form":form})




def view_business(request):
   user = request.user
   profile = Profile.find_profile_by_id(user)
   # neighborhood = Neighborhood.find_neighborhood(profile.neighborhood_id.id)
   # businesses = Business.all_business()
   return render(request,'business.html',{"user":user,"profile":profile,})




@login_required(login_url='/accounts/login/')
def new_post(request):

    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect( index ) 
    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})


@login_required(login_url='/accounts/login/')
def post(request):
    post = Post.get_post()
    return render(request,'post.html',{'post':post})

def leave_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST )
        if form.is_valid():
            neighborhoods = Neighborhood()
            hood=form.save(commit=False)
            hood.save()
            return render(request,'leave.html',{"form": form})



 




