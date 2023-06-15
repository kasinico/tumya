from django.db import models

# Create your models here.
# models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    # Other item fields as needed

class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # Other cart fields as needed

