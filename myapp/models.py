from django.db import models

# Create your models here.
class Account_Details(models.Model):
    First_Name = models.CharField(max_length = 30)
    Last_Name = models.CharField(max_length = 30)
    Emails = models.CharField(max_length = 30)
    Contac_no = models.IntegerField()
    Address = models.TextField()