
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.show_compose_view, name="new_post"),
    
    #API ROUTERS
    path('compose_post', views.compose_post, name="compose"),
    path('render_posts', views.show_posts, name="all_posts")
]
