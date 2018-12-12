from django.db import models

# pk 1
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

class Goods(models.Model):
    author = models.CharField(max_length=250)
    good_title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

