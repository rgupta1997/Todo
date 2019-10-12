from django.db import models


class User(models.Model):
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.f_name


class Todoo(models.Model):
    types=(( 'created','Created'),('inprogress','inprogress'),('done','Done'))
    desc=models.CharField(max_length=500)
    title=models.CharField(max_length=200)
    status=models.CharField(max_length=100,choices=types)
    created_time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
# Create your models here.
