from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    medium_cover_image = models.URLField()
    year = models.IntegerField()
    rating = models.FloatField()
    genres = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    date_uploaded = models.DateTimeField()
    quality = models.CharField(max_length=50)
    runtime = models.IntegerField()
    summary = models.TextField()
    file_path = models.CharField(max_length=255)  # or models.FileField(upload_to='movies/')


    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    flagged = models.BooleanField(default=False)
    report_count = models.PositiveIntegerField(default=0)