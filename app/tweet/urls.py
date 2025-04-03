from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', tweet_list, name='tweet_list'),
    path('create/', tweet_create, name='tweet_create'),
    path('edit/<int:id>',tweet_edit,name='tweet_edit'),
    path('delete/<int:id>',tweet_delete, name='tweet_delete'),
]