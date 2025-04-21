from django.contrib.auth.models import AbstractUser
from django.forms.models import model_to_dict
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    author_id = models.ForeignKey("User", on_delete=models.PROTECT)
    author_name = models.CharField(max_length=50)
    content = models.TextField(blank=False)
    #excerpt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    nb_of_views = models.IntegerField(default=0)
    nb_of_likes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "author_id": model_to_dict(self.author_id),
            "author_name":self.author_name,
            "content": self.content,
            "created_at": self.created_at.strftime("%b %d, %Y, %I:%M %p"),
            "nb_of_views": self.nb_of_views,
            "nb_of_likes": self.nb_of_likes,
            "liked": self.liked
        }