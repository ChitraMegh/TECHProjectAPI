from django.db import models

class ProductMainModel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unique_code = models.CharField(max_length=255, unique=True)
    SIZE_CHOICES = [
        ('high', 'High'),
        ('low', 'Low'),
        ('medium', 'Medium'),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)

class ProductColourModel(models.Model):
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    COLOUR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    color = models.CharField(max_length=10, choices=COLOUR_CHOICES)

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
    image = models.ImageField()