import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse


from .models import User, Post


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    next_url = request.GET.get('next')
    current_url = next_url if next_url else reverse("index")

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(current_url)
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password.",
                "next":next_url
            })
    else:
        return render(request, "network/login.html", {'next': next_url})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def compose_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get("content")

        post = Post(
            author_id = request.user,
            author_name = request.user,
            content = content
        ) 
        post.save()
    return JsonResponse({"message": "content was post successfully."}, status=201)
    
    
def show_posts(request):
    
    posts = Post.objects.select_related('author_id').all()        
    posts = posts.order_by("-created_at").all()
    posts = [post_item.serialize() for post_item in posts ]

    return JsonResponse(posts, safe=False) 

@login_required
def show_compose_view(request):
    return render(request, "network/new_post_view.html")

""" def show_following_view(request):
    return render(request, "network/following_page.html")

def profile_page_view(request):
    return render(request, "network/profile_page.html") """