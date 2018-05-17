from django.contrib import admin
from django.urls import path, include
from base import urls
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
