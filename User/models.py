from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    username=models.CharField(max_length=25,verbose_name="username")
    name=models.CharField(max_length=20,default="noName",verbose_name="name")
    password=models.CharField(max_length=20,verbose_name="password")
    email=models.EmailField()
    userCode=models.CharField(default=" ",max_length=100,verbose_name="User Code")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-username']