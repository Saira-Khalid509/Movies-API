from django.contrib import admin
from .models import Movie, UserProfile, Comment

# Register your models here.

admin.site.register(Movie)
admin.site.register(UserProfile)
admin.site.register(Comment)
