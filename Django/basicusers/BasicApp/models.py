from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #Additional models
    portfolio_site = models.URLField(blank=True,default='')
    profile_pic = models.ImageField(upload_to='ProfilePics',blank = True)

    def __str__(self):
        return self.user.username
