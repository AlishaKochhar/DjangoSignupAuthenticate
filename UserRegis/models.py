from django.db import models

# Create your models here.

class UserRegis(models.Model):
    first_name=models.CharField(max_length=120,null=True,blank=True)
    last_name=models.CharField(max_length=120,null=True,blank=True)
    username=models.CharField(max_length=120,null=True,blank=True)
    email=models.EmailField()
    password=models.CharField(max_length=120,null=True,blank=True)
    timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
    updated=models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self) :
        return str(self.first_name)+"---"+str(self.email)
