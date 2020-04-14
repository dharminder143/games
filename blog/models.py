from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # slug = models.SlugField()

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.CharField(max_length=50)
    gamename = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    GameURL = models.TextField()
    IMGURL = models.ImageField( upload_to='images/')
