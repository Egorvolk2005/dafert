from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class Post(models.Model):
    title = models.CharField(max_length=200) 
    text = models.TextField() 
    pub_date = models.DateTimeField(auto_now_add=True) 
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    answer_the_tweet_id = models.IntegerField()

    def __str__(self):
        return self.title 