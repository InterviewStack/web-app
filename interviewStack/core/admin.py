from django.contrib import admin
from .models import UserProfile, UserInterest, Interaction, Tag

admin.site.register(UserProfile)
admin.site.register(UserInterest)
admin.site.register(Interaction)
admin.site.register(Tag)
