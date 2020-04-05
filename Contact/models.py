from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    name = models.CharField(max_length=20, default="noName", verbose_name="name")
    email = models.EmailField()
    message=models.CharField(max_length=500,verbose_name="message")
    def __str__(self):
        return self.name

    class Meta:
        ordering=['-name']