import datetime

from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=True)  # Add tags
    admin_notes = models.TextField(blank=True)  # Add admin notes

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='categories', blank=True)

    def __str__(self):
        return self.name
