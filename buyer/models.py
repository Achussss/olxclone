from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Brand(models.Model):
    brand_name = models.CharField(max_length=200)

    def __str__(self) :
        return self.brand_name

class Products(models.Model):
    CATEGORY_CHOICES = (
        ('ELECTRONICS', 'Electronics'),
        ('FASHION', 'Fashion'),
        ('HOME', 'Home'),
        ('SPORTS', 'Sports'),
        ('OTHER', 'Other'),
    )
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    photo = models.ImageField(upload_to='product_photos', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200)

    options =(
          ("for sale", "for sale"),
        ("exchange", "exchange"), 
        ("sold out", "sold out"),
        ("rent", "rent")
    )

    status = models.CharField(max_length=200, choices=options, default="for sale")

    def __str__(self):
        return self.name
        
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(null=True, upload_to="profile.images")
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)

    


class Notifications(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    options = (
        ("sent", "sent"),
        ("cancelled", "cancelled"),
        ("pending","pending")
    )
    status = models.CharField(max_length=200, choices=options, default="sent")
    
