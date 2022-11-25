from django.contrib import admin
from .models import Movie, Comment, Profile

# Register your models here.
admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Profile)