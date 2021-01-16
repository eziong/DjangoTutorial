from django.urls import path

from . import views
urlpatterns = [
    path('',views._index, name='index'),
    path('<int:user_id>/',views._detail, name='detail'),
    path('login/',views._login, name='login'),
    path('signup/',views._signup,name='signup'),
    path('logout/',views._logout, name="logout"),
]