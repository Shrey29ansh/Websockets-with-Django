from django.db import models
import uuid
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

# Create your models here.
class Testdb(models.Model):
    message= models.CharField(max_length=50)
    time_sent = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.message

class Friends(models.Model):
    from_username = models.ForeignKey(User, related_name='userone',on_delete=models.CASCADE)
    to_username = models.ForeignKey(User,related_name='usertwo', on_delete=models.CASCADE)
    relation_name = models.IntegerField(unique=True)
    friend_request = models.CharField(max_length=15,default='NOT SENT')
    friend_status =models.BooleanField(default=False)
