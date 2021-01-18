from django.urls import path

from . import views

urlpatterns = [
    path('',views._index, name='index'),
    path('/detail',views._detail, name='detail'),
]