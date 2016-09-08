from django.db import models

# Create your models here.

class Research(models.Model):
    Author=models.CharField(max_length=250)
    Department_name=models.CharField(max_length=500)
    University_name=models.CharField(max_length=500)
    Address=models.CharField(default=0,max_length=600)

    def __str__(self):
        return self.Author + '-' + self.University_name

class Papers(models.Model):
    research=models.ForeignKey(Research,on_delete=models.CASCADE)
    Journal_Paper=models.CharField(max_length=500)
    Paper_Title=models.CharField(max_length=400)
    
