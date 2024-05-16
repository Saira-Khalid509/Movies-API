from django.contrib.auth.models import User
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    genres = models.CharField(max_length=100)
    url = models.URLField()
    summary = models.TextField()
    size = models.CharField(max_length=20)
    date_uploaded = models.DateTimeField()
    runtime = models.IntegerField()
    quality = models.CharField(max_length=20)
    medium_cover_image = models.ImageField()
    large_cover_image = models.ImageField()
    small_cover_image = models.ImageField()

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