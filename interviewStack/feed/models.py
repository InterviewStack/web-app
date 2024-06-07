from django.db import models
from core import UserProfile

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    youtube_embed_link = models.URLField(null=True, blank=True)
    post_link = models.URLField(unique=True)
    total_views = models.IntegerField(unique=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey(Comment, on_delete=modeles.CASCADE, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
