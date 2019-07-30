from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField('Name of the Category', max_length=200)
    category_description = models.CharField('Description of the Category', max_length=500)

    def __str__(self):
        return self.category_name