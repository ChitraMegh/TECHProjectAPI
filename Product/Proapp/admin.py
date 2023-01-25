from django.contrib import admin
from .models import ProductMainModel, ProductColourModel, ProductImageModel

admin.site.register(ProductMainModel)
admin.site.register(ProductColourModel)
admin.site.register(ProductImageModel)


# Register your models here.
