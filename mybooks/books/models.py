from django.urls import reverse
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    status = models.CharField(max_length=100)
    image = models.CharField(max_length=500, default='https://images-na.ssl-images-amazon.com/images/I/81l3rZK4lnL.jpg')

    def get_absolute_url(self):
        return reverse("books:detail",kwargs={'pk':self.pk})
    

    def __str__(self):
        return self.name