from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=1024)
    short_description = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
