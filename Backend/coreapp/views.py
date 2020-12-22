from django.shortcuts import render
from rest_framework import views,generics,status
from .models import Testdb,Friends
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from .serializers import PostSerializer
from rest_framework.authtoken.models import Token
from django.core import serializers
import json

#from faker import Faker      

User = get_user_model()

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

class SearchFriend(views.APIView):
    permission_classes =[IsAuthenticated,]
    def get(self,request,format=None):
        myuser = request.user
        if User:
            try:
                username = request.data.get('friend_name')
                friend_exist = User.objects.values('first_name','last_name','id','username').get(username=username)
                relation_name = int(friend_exist['id'])+int(myuser.pk)
                request_status = Friends.objects.filter(relation_name=relation_name).values()
                if request_status:
                    request_status = request_status[0]['friend_request']
                else:
                    request_status = "NOT SENT"
                message = {
                        'Name':str(friend_exist['first_name']+" "+friend_exist['last_name']),
                        "Username":str(friend_exist['username']),
                        "friend_request":request_status
                    }
                return Response(message,status=status.HTTP_200_OK)
            except ObjectDoesNotExist as identifier:
                identifier = {'message':"User Not Found."}
                return Response(identifier,status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Not Authenticated")

class SendRequest(views.APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        from_user = request.user
        to_user=User.objects.get(username=request.data.get('friend_name'))
        relation_name = int(to_user.pk)+int(from_user.pk)
        request_status = Friends.objects.filter(relation_name=relation_name).values()
        if request_status:
            identifier = {'message':request_status[0]['friend_request']} 
        else:
            try:
                friends = Friends.objects.create(from_username = from_user,to_username=to_user,friend_request="SENT",relation_name=relation_name)
                friends.save()
                identifier = {'message':"Request sent"}
            except IntegrityError as identifier:
                identifier = {'message':"Request Already sent"}
                return Response(identifier,status=status.HTTP_404_NOT_FOUND)
        return Response(identifier,status=status.HTTP_200_OK)

class CheckFriendRequest(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer
    def get_queryset(self):
        friend_requests=""
        myuser=self.request.user
        friend_requests = Friends.objects.filter(to_username=myuser,friend_status=False)
        return friend_requests

"""  
class Fakedata(views.APIView):
    def get(self,request,format=None):
        fake = Faker()
        for i in range(0,1 ):
            user = User.objects.create_user(fake.user_name(),fake.email(),'tumpassaaye')
            user.last_name = fake.last_name()
            user.first_name = fake.first_name()
            user.save()
        return Response("hello") """