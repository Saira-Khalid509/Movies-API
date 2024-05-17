from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
   class Movie(models.Model):
    title = models.CharField(max_length=255)
    medium_cover_image = models.ImageField(null=True, blank=True)  # Allow null and blank values
    year = models.IntegerField(default=0)  # Set default value
    rating = models.FloatField(default=0.0)  # Set default value
    genres = models.CharField(max_length=255, null=True, blank=True)  # Allow null and blank values
    size = models.CharField(max_length=50, null=True, blank=True)  # Allow null and blank values
    date_uploaded = models.DateTimeField(null=True, blank=True)  # Allow null and blank values
    quality = models.CharField(max_length=50, null=True, blank=True)  # Allow null and blank values
    runtime = models.IntegerField(default=0)  # Set default value
    summary = models.TextField(max_length=5000, null=True, blank=True)  # Allow null and blank values
    file_path = models.CharField(max_length=255, null=True, blank=True)  # or models.FileField(upload_to='movies/')


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