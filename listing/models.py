from django.db import models
from django.urls import reverse

# pk 1
class Category(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    category_logo = models.CharField(max_length=600)
    def get_absolute_url(self):
        return reverse('listing:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + ' - ' + self.description

class Listing(models.Model):
    author = models.CharField(max_length=250)
    listing_title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.author + ' - ' + self.listing_title

