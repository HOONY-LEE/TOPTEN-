from django.shortcuts import render
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Genre, Movie, Comment, Profile, Message
from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer, ProfileSerializer, MessageSerializer

# Create your views here.
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def home(request, order):
    movies = Movie.objects.all().order_by(order).filter(~Q(vote_avg=0.0))
    # print(movies[0].title)
    # print(movies[0].genres.filter(genre_id = 28))
    # movies = get_list_or_404(Movie)
    context = PageNumberPagination().paginate_queryset(movies, request)
    serializer = MovieListSerializer(context, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recent(request):
    movies = Movie.objects.filter(released_date__lte = '2022-11-25').order_by('-released_date')
    context = PageNumberPagination().paginate_queryset(movies, request)
    serializer = MovieListSerializer(context, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def soon(request):
    movies = Movie.objects.filter(released_date__gte = '2022-11-25').order_by('released_date')
    context = PageNumberPagination().paginate_queryset(movies, request)
    serializer = MovieListSerializer(context, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search(request, keyword):
    movies = Movie.objects.filter(title__contains = keyword).order_by('-popularity')
    context = PageNumberPagination().paginate_queryset(movies, request)
    serializer = MovieListSerializer(context, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre(request, genre_pk):
    genre_obj = Genre.objects.filter(pk=genre_pk)
    movies = Movie.objects.filter(genres__in = genre_obj).order_by('-popularity')
    context = PageNumberPagination().paginate_queryset(movies, request)
    serializer = MovieListSerializer(context, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def likes(request, movie_pk, profile_pk):
    movie = Movie.objects.get(pk=movie_pk)
    profile = Profile.objects.get(pk=profile_pk)
    # if request.user in article.like_users.all():
    if movie.like_profiles.filter(pk=profile_pk).exists():
        # 좋아요 취소 (remove)
        movie.like_profiles.remove(profile)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        # 좋아요 추가 (add)
        movie.like_profiles.add(profile)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['POST'])
def wishs(request, movie_pk, profile_pk):
    movie = Movie.objects.get(pk=movie_pk)
    profile = Profile.objects.get(pk=profile_pk)
    # if request.user in article.like_users.all():
    if movie.wish_profiles.filter(pk=profile_pk).exists():
        # 좋아요 취소 (remove)
        movie.wish_profiles.remove(profile)
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        # 좋아요 추가 (add)
        movie.wish_profiles.add(profile)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def topten(request, movie_pk, profile_pk):
    movie = Movie.objects.get(pk=movie_pk)
    profile = Profile.objects.get(pk=profile_pk)
    if not profile.movie1:
        serializer = ProfileSerializer(profile, data={'movie1': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie1=movie)
            return Response(serializer.data)
    elif not profile.movie2:
        serializer = ProfileSerializer(profile, data={'movie2': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie2=movie)
            return Response(serializer.data)
    elif not profile.movie3:
        serializer = ProfileSerializer(profile, data={'movie3': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie3=movie)
            return Response(serializer.data)
    elif not profile.movie4:
        serializer = ProfileSerializer(profile, data={'movie4': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie4=movie)
            return Response(serializer.data)
    elif not profile.movie5:
        serializer = ProfileSerializer(profile, data={'movie5': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie5=movie)
            return Response(serializer.data)
    elif not profile.movie6:
        serializer = ProfileSerializer(profile, data={'movie6': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie6=movie)
            return Response(serializer.data)
    elif not profile.movie7:
        serializer = ProfileSerializer(profile, data={'movie7': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie7=movie)
            return Response(serializer.data)
    elif not profile.movie8:
        serializer = ProfileSerializer(profile, data={'movie8': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie8=movie)
            return Response(serializer.data)
    elif not profile.movie9:
        serializer = ProfileSerializer(profile, data={'movie9': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie9=movie)
            return Response(serializer.data)
    elif not profile.movie10:
        serializer = ProfileSerializer(profile, data={'movie10': movie}, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie10=movie)
            return Response(serializer.data)
    else:
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

@api_view(['GET'])
def comment(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comments = Comment.objects.filter(movie=movie).order_by('-created_at')[:5]
    # comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, movie_pk, profile_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    profile = get_object_or_404(Profile, pk=profile_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=profile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
def profile_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.filter(user=request.user)
        # profiles = get_list_or_404(Profile)
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def profile_detail(request, profile_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    profile = get_object_or_404(Profile, pk=profile_pk)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def topten_edit(request, profile_pk, grade):
    profile = Profile.objects.get(pk=profile_pk)

    if request.method == 'PUT':
        if grade == 1 and profile.movie2:
            serializer = ProfileSerializer(profile, data={
                'movie1': profile.movie2,
                'movie2': profile.movie1,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie1 = profile.movie2,
                    movie2 = profile.movie1,
                    )
            return Response(serializer.data)
            # movie1 = profile.movie1
            # serializer = ProfileSerializer(profile, data={'movie1': profile.movie2}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie1 = profile.movie2)
            # serializer = ProfileSerializer(profile, data={'movie2': movie1}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie2 = movie1)
            # return Response(serializer.data)
        elif grade == 2 and profile.movie3:
            serializer = ProfileSerializer(profile, data={
                'movie3': profile.movie2,
                'movie2': profile.movie3,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie3 = profile.movie2,
                    movie2 = profile.movie3,
                    )
            return Response(serializer.data)
            # movie2 = profile.movie2
            # serializer = ProfileSerializer(profile, data={'movie2': profile.movie3}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie2 = profile.movie3)
            # serializer = ProfileSerializer(profile, data={'movie3': movie2}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie3 = movie2)
            # return Response(serializer.data)
        elif grade == 3 and profile.movie4:
            serializer = ProfileSerializer(profile, data={
                'movie3': profile.movie4,
                'movie4': profile.movie3,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie3 = profile.movie4,
                    movie4 = profile.movie3,
                    )
            return Response(serializer.data)
        elif grade == 4 and profile.movie5:
            serializer = ProfileSerializer(profile, data={
                'movie5': profile.movie4,
                'movie4': profile.movie5,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie5 = profile.movie4,
                    movie4 = profile.movie5,
                    )
            return Response(serializer.data)
        elif grade == 5 and profile.movie6:
            serializer = ProfileSerializer(profile, data={
                'movie5': profile.movie6,
                'movie6': profile.movie5,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie5 = profile.movie6,
                    movie6 = profile.movie5,
                    )
            return Response(serializer.data)
        elif grade == 6 and profile.movie7:
            serializer = ProfileSerializer(profile, data={
                'movie7': profile.movie6,
                'movie6': profile.movie7,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie7 = profile.movie6,
                    movie6 = profile.movie7,
                    )
            return Response(serializer.data)
        elif grade == 7 and profile.movie8:
            serializer = ProfileSerializer(profile, data={
                'movie7': profile.movie8,
                'movie8': profile.movie7,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie7 = profile.movie8,
                    movie8 = profile.movie7,
                    )
            return Response(serializer.data)
        elif grade == 8 and profile.movie9:
            serializer = ProfileSerializer(profile, data={
                'movie9': profile.movie8,
                'movie8': profile.movie9,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie9 = profile.movie8,
                    movie8 = profile.movie9,
                    )
            return Response(serializer.data)
        elif grade == 9 and profile.movie10:
            serializer = ProfileSerializer(profile, data={
                'movie9': profile.movie10,
                'movie10': profile.movie9,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie9 = profile.movie10,
                    movie10 = profile.movie9,
                    )
            return Response(serializer.data)
        else:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        if grade == 1:
            serializer = ProfileSerializer(profile, data={
                'movie1': profile.movie2,
                'movie2': profile.movie3,
                'movie3': profile.movie4,
                'movie4': profile.movie5,
                'movie5': profile.movie6,
                'movie6': profile.movie7,
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie1 = profile.movie2,
                    movie2 = profile.movie3,
                    movie3 = profile.movie4,
                    movie4 = profile.movie5,
                    movie5 = profile.movie6,
                    movie6 = profile.movie7,
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
            # if profile.movie2:
            #     serializer = ProfileSerializer(profile, data={'movie1': profile.movie2}, partial=True)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save(movie1 = profile.movie2)
            # else:
            #     serializer = ProfileSerializer(profile, data={'movie1': None}, partial=True)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save(movie1 = None)
            #     return Response(serializer.data)
            # if profile.movie3:
            #     serializer = ProfileSerializer(profile, data={'movie2': profile.movie3}, partial=True)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save(movie2 = profile.movie3)
            # else:
            #     serializer = ProfileSerializer(profile, data={'movie2': None}, partial=True)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save(movie2 = None)
            # serializer = ProfileSerializer(profile, data={'movie3': None}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie3 = None)
            #     return Response(serializer.data)
        elif grade == 2:
            serializer = ProfileSerializer(profile, data={
                'movie2': profile.movie3,
                'movie3': profile.movie4,
                'movie4': profile.movie5,
                'movie5': profile.movie6,
                'movie6': profile.movie7,
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie2 = profile.movie3,
                    movie3 = profile.movie4,
                    movie4 = profile.movie5,
                    movie5 = profile.movie6,
                    movie6 = profile.movie7,
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
            # if profile.movie3:
            #     serializer = ProfileSerializer(profile, data={'movie2': profile.movie3}, partial=True)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save(movie2 = profile.movie3)
            # else:
            #     serializer = ProfileSerializer(profile, data={'movie2': None}, partial=True)
            #     if serializer.is_valid(raise_exception=True):
            #         serializer.save(movie2 = None)
            # serializer = ProfileSerializer(profile, data={'movie3': None}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie3 = None)
            #     return Response(serializer.data)
        elif grade == 3:
            serializer = ProfileSerializer(profile, data={
                'movie3': profile.movie4,
                'movie4': profile.movie5,
                'movie5': profile.movie6,
                'movie6': profile.movie7,
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie3 = profile.movie4,
                    movie4 = profile.movie5,
                    movie5 = profile.movie6,
                    movie6 = profile.movie7,
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
            # serializer = ProfileSerializer(profile, data={'movie3': None}, partial=True)
            # if serializer.is_valid(raise_exception=True):
            #     serializer.save(movie3 = None)
            #     return Response(serializer.data)
        elif grade == 4:
            serializer = ProfileSerializer(profile, data={
                'movie4': profile.movie5,
                'movie5': profile.movie6,
                'movie6': profile.movie7,
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie4 = profile.movie5,
                    movie5 = profile.movie6,
                    movie6 = profile.movie7,
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
        elif grade == 5:
            serializer = ProfileSerializer(profile, data={
                'movie5': profile.movie6,
                'movie6': profile.movie7,
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie5 = profile.movie6,
                    movie6 = profile.movie7,
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
        elif grade == 6:
            serializer = ProfileSerializer(profile, data={
                'movie6': profile.movie7,
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie6 = profile.movie7,
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
        elif grade == 7:
            serializer = ProfileSerializer(profile, data={
                'movie7': profile.movie8,
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie7 = profile.movie8,
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
        elif grade == 8:
            serializer = ProfileSerializer(profile, data={
                'movie8': profile.movie9,
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie8 = profile.movie9,
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
        elif grade == 9:
            serializer = ProfileSerializer(profile, data={
                'movie9': profile.movie10,
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie9 = profile.movie10,
                    movie10 = None,
                    )
            return Response(serializer.data)
        elif grade == 10:
            serializer = ProfileSerializer(profile, data={
                'movie10': None,
                }, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save(
                    movie10 = None,
                    )
            return Response(serializer.data)
        else:
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)

@api_view(['POST'])
def follow(request, to_pk, from_pk):
    if request.user.is_authenticated:
        me = Profile.objects.get(pk=to_pk)
        you = Profile.objects.get(pk=from_pk)
        if me != you:
            # if me in you.followers.all():
            if you.followers.filter(pk=me.pk).exists():
                # 언팔로우
                you.followers.remove(me)
            else:
                # 팔로우
                you.followers.add(me)
        serializer = ProfileSerializer(me)
        return Response(serializer.data, status=status.HTTP_200_OK)
    serializer = ProfileSerializer(me)
    return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def message(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    messages = Message.objects.filter(to_user=profile).order_by('-created_at')[:5]
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def message_send(request, to_pk, from_pk):
    to_user = get_object_or_404(Profile, pk=to_pk)
    from_user = get_object_or_404(Profile, pk=from_pk)
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(to_user=to_user, from_user=from_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def recommend(request, profile_pk, gender, method):
    user = get_object_or_404(Profile, pk=profile_pk)
    if method == 1:
        if gender == 3:
            profiles = Profile.objects.filter(~Q(id=user.id)).order_by("?")
        else:
            profiles = Profile.objects.filter(~Q(id=user.id)).filter(gender=3-gender).order_by("?")
    elif method == 2:
        if gender == 3:
            profiles = Profile.objects.filter(~Q(id=user.id)).filter(Q(movie1=user.movie1) | Q(movie2=user.movie1) | Q(movie3=user.movie1) | Q(movie4=user.movie1) | Q(movie5=user.movie1)).filter(Q(movie1=user.movie2) | Q(movie2=user.movie2) | Q(movie3=user.movie2) | Q(movie4=user.movie2) | Q(movie5=user.movie2) | Q(movie6=user.movie2)).filter(Q(movie1=user.movie3) | Q(movie2=user.movie3) | Q(movie3=user.movie3) | Q(movie4=user.movie3) | Q(movie5=user.movie3) | Q(movie6=user.movie3) | Q(movie7=user.movie3)).filter(Q(movie1=user.movie4) | Q(movie2=user.movie4) | Q(movie3=user.movie4) | Q(movie4=user.movie4) | Q(movie5=user.movie4) | Q(movie6=user.movie4) | Q(movie7=user.movie4) | Q(movie8=user.movie4)).filter(Q(movie1=user.movie5) | Q(movie2=user.movie5) | Q(movie3=user.movie5) | Q(movie4=user.movie5) | Q(movie5=user.movie5) | Q(movie6=user.movie5) | Q(movie7=user.movie5) | Q(movie8=user.movie5) | Q(movie9=user.movie5)).order_by("?")
        else:
            profiles = Profile.objects.filter(~Q(id=user.id)).filter(Q(movie1=user.movie1) | Q(movie2=user.movie1) | Q(movie3=user.movie1) | Q(movie4=user.movie1) | Q(movie5=user.movie1)).filter(Q(movie1=user.movie2) | Q(movie2=user.movie2) | Q(movie3=user.movie2) | Q(movie4=user.movie2) | Q(movie5=user.movie2) | Q(movie6=user.movie2)).filter(Q(movie1=user.movie3) | Q(movie2=user.movie3) | Q(movie3=user.movie3) | Q(movie4=user.movie3) | Q(movie5=user.movie3) | Q(movie6=user.movie3) | Q(movie7=user.movie3)).filter(Q(movie1=user.movie4) | Q(movie2=user.movie4) | Q(movie3=user.movie4) | Q(movie4=user.movie4) | Q(movie5=user.movie4) | Q(movie6=user.movie4) | Q(movie7=user.movie4) | Q(movie8=user.movie4)).filter(Q(movie1=user.movie5) | Q(movie2=user.movie5) | Q(movie3=user.movie5) | Q(movie4=user.movie5) | Q(movie5=user.movie5) | Q(movie6=user.movie5) | Q(movie7=user.movie5) | Q(movie8=user.movie5) | Q(movie9=user.movie5)).filter(gender=3-gender).order_by("?")
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)