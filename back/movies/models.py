from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    genre_id = models.IntegerField()
    name = models.CharField(max_length=50)

class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200, null=True)
    backdrop_path = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    genres_info = models.JSONField()
    actor = models.JSONField()
    director = models.JSONField()
    trailer = models.JSONField()
    watch = models.JSONField()
    similar = models.JSONField()
    # like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # wish_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='wish_movies')

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.IntegerField()
    img = models.IntegerField()
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movies = models.ManyToManyField(Movie, related_name='like_profiles')
    wish_movies = models.ManyToManyField(Movie, related_name='wish_profiles')
    movie1 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie1")
    movie2 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie2")
    movie3 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie3")
    movie4 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie4")
    movie5 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie5")
    movie6 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie6")
    movie7 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie7")
    movie8 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie8")
    movie9 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie9")
    movie10 = models.ForeignKey(Movie, null=True, on_delete=models.SET_NULL, related_name="movie10")

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE) # user를 profile로 바꿀려면 views도 건드려야 할것이다.
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    from_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="message_send")
    to_user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="message_recive")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)