from django.db import models


# Create your models here.

class Partymenu(models.Model):
    category = models.CharField(max_length=100)
    item_id = models.CharField(max_length=10)
    item = models.CharField(max_length=100)
    small_tray = models.IntegerField()
    large_tray = models.IntegerField()
    img = models.ImageField(upload_to='images')
    up_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    