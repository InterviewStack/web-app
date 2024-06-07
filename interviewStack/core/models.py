from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profile_images/')
    bio = models.TextField()
    links = models.TextField()

class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255)
    scores = models.CharField(max_length=255)

class Interaction(models.Model):
    tag_id = models.IntegerField()
    action = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    company_name = models.CharField(max_length=255)
    content_type = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255, null=True, blank=True)
    domain = models.CharField(max_length=255)
    technical_tags = models.CharField(max_length=255)
