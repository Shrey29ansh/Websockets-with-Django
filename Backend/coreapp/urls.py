from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('friend/search/', views.SearchFriend.as_view(), name='index'),
    path('friend/request/check/', views.CheckFriendRequest.as_view(), name='index'),
    path('friend/request/send/', views.SendRequest.as_view(), name='index'),
]
"""     
ath('my/fakedata/', views.Fakedata.as_view(), name='index'),
path('friend/search/', views.SearchFriend.as_view(), name='index'),
    path('friend/request/check/', views.CheckFriendRequest.as_view(), name='index'),
    path('friend/request/send/', views.SendRequest.as_view(), name='index'),
 """