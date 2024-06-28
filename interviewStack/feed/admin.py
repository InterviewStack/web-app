from django.contrib import admin
from .models import Post, Comment, Likes, ReadingList

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(ReadingList)
