from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('prod_cat', args=[self.slug])


class Prod(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to='products')
    des = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get__url(self):
        return reverse('details', args=[self.category.slug, self.slug])
