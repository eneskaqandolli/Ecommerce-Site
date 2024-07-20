from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title
    
class Order(models.Model):
    items = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
    total = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return f"{self.name}'s order"