from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=50)
    gamename = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    GameURL = models.TextField()
    IMGURL = models.ImageField( upload_to='images/')
