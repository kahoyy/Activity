from django.urls import path
from .views import create_tweet, tweet_success

urlpatterns = [
    path('create/', create_tweet, name='create_tweet'),
    path('success/', tweet_success, name='tweet_success'),
]
