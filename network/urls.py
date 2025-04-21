
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    #API ROUTERS
    path('compose_post', views.compose_post, name="compose"),
    path('render_posts', views.show_posts, name="all_posts")
]
