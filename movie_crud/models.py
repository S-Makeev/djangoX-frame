from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=64)
    user_name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(default="generic description")

    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
        return reverse("movie_detail", args=[str(self.id)])
# Create your models here.
