from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'content', 'created_at', 'nb_of_views', 'nb_of_likes', 'liked')
    
admin.site.register(Post, PostAdmin)