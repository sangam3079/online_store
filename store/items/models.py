from django.db import models

# Create your models here.
class Item(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    price = models.IntegerField()


