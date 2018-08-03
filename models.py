from django.db import models


# Create your models here.
class Sitepages(models.Model):
    title = models.CharField(max_length=250)
    img_1 = models.ImageField(upload_to='media/')
    img_2 = models.ImageField(upload_to='media/')
    img_3 = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title + " \n "
