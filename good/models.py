from django.db import models

# pk 1
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    category_logo = models.CharField(max_length=600)
    def __str__(self):
        return self.name + ' - ' + self.description

class Good(models.Model):
    author = models.CharField(max_length=250)
    good_title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.author + ' - ' + self.good_title

