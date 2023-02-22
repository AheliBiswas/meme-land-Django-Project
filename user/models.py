from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=2000,null=True,blank=True)
    verification_id = models.UUIDField(default=uuid.uuid4,unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
