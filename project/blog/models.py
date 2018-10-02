from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    # Each class is own table, each attribute is field
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True
    # date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    # one to many relationship. 
    # on_delete = if user deleted, delete post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title