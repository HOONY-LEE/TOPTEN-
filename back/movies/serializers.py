from rest_framework import serializers

from .models import Movie, Comment, Profile, Message


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.name', read_only=True)
    userprofile = serializers.IntegerField(source='user.img', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user',)

class MessageSerializer(serializers.ModelSerializer):
    from_username = serializers.CharField(source='from_user.name', read_only=True)
    to_username = serializers.CharField(source='to_user.name', read_only=True)
    from_userprofile = serializers.IntegerField(source='from_user.img', read_only=True)
    to_userprofile = serializers.IntegerField(source='to_user.img', read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('to_user', 'from_user')

class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'like_movies', 'wish_movies', 'movie1', 'movie2', 'movie3', 'movie4', 'movie5', 'movie6', 'movie7', 'movie8', 'movie9', 'movie10', 'followings')

class ProfileSerializer(serializers.ModelSerializer):
    message_recive = MessageSerializer(many=True, read_only=True)
    message_send = MessageSerializer(many=True, read_only=True)
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    movie1_title = serializers.JSONField(source='movie1.title', read_only=True)
    movie2_title = serializers.JSONField(source='movie2.title', read_only=True)
    movie3_title = serializers.JSONField(source='movie3.title', read_only=True)
    movie4_title = serializers.JSONField(source='movie4.title', read_only=True)
    movie5_title = serializers.JSONField(source='movie5.title', read_only=True)
    movie6_title = serializers.JSONField(source='movie6.title', read_only=True)
    movie7_title = serializers.JSONField(source='movie7.title', read_only=True)
    movie8_title = serializers.JSONField(source='movie8.title', read_only=True)
    movie9_title = serializers.JSONField(source='movie9.title', read_only=True)
    movie10_title = serializers.JSONField(source='movie10.title', read_only=True)
    movie1_poster_path = serializers.JSONField(source='movie1.poster_path', read_only=True)
    movie2_poster_path = serializers.JSONField(source='movie2.poster_path', read_only=True)
    movie3_poster_path = serializers.JSONField(source='movie3.poster_path', read_only=True)
    movie4_poster_path = serializers.JSONField(source='movie4.poster_path', read_only=True)
    movie5_poster_path = serializers.JSONField(source='movie5.poster_path', read_only=True)
    movie6_poster_path = serializers.JSONField(source='movie6.poster_path', read_only=True)
    movie7_poster_path = serializers.JSONField(source='movie7.poster_path', read_only=True)
    movie8_poster_path = serializers.JSONField(source='movie8.poster_path', read_only=True)
    movie9_poster_path = serializers.JSONField(source='movie9.poster_path', read_only=True)
    movie10_poster_path = serializers.JSONField(source='movie10.poster_path', read_only=True)
    movie1_genres_info = serializers.JSONField(source='movie1.genres_info', read_only=True)
    movie2_genres_info = serializers.JSONField(source='movie2.genres_info', read_only=True)
    movie3_genres_info = serializers.JSONField(source='movie3.genres_info', read_only=True)
    movie4_genres_info = serializers.JSONField(source='movie4.genres_info', read_only=True)
    movie5_genres_info = serializers.JSONField(source='movie5.genres_info', read_only=True)
    movie6_genres_info = serializers.JSONField(source='movie6.genres_info', read_only=True)
    movie7_genres_info = serializers.JSONField(source='movie7.genres_info', read_only=True)
    movie8_genres_info = serializers.JSONField(source='movie8.genres_info', read_only=True)
    movie9_genres_info = serializers.JSONField(source='movie9.genres_info', read_only=True)
    movie10_genres_info = serializers.JSONField(source='movie10.genres_info', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ('user', 'like_movies', 'wish_movies', 'movie1', 'movie2', 'movie3', 'movie4', 'movie5', 'movie6', 'movie7', 'movie8', 'movie9', 'movie10', 'followings')