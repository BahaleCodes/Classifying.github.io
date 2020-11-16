from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    published = models.DateField(null=True, default=None, blank=True)
    cover = models.FileField(upload_to='covers/', blank=True)