from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discountPercentage = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    thumbnail = models.URLField()

    def __str__(self):
        return f"{self.title}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.URLField()

    def __str__(self):
        return f"Image of {self.product.title}"


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    body = models.TextField()
    postId = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.body
    
    
