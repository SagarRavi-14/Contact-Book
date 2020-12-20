from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name
 
    