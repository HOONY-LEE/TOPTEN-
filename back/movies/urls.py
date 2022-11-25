from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('home/<str:order>/', views.home),
    path('recent/', views.recent),
    path('soon/', views.soon),
    path('search/<str:keyword>/', views.search),
    path('genre/<int:genre_pk>/', views.genre),
    path('<int:movie_pk>/', views.detail),
    path('<int:movie_pk>/likes/<int:profile_pk>/', views.likes),
    path('<int:movie_pk>/wishs/<int:profile_pk>/', views.wishs),
    path('<int:movie_pk>/topten/<int:profile_pk>/', views.topten),
    path('<int:movie_pk>/comments/', views.comment),
    path('<int:movie_pk>/comments/<int:profile_pk>/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('profiles/', views.profile_list),
    path('profiles/<int:profile_pk>/', views.profile_detail),
    path('profiles/<int:profile_pk>/topten/<int:grade>/', views.topten_edit),
    path('profiles/<int:profile_pk>/message/', views.message),
    path('profiles/<int:to_pk>/message/<int:from_pk>/', views.message_send),
    path('profiles/<int:to_pk>/follow/<int:from_pk>/', views.follow),
    path('recommend/<int:profile_pk>/<int:gender>/<int:method>/', views.recommend),
]