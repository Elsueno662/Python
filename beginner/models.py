from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.product_name

class Customer(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    purchase_date = models.DateField()

    def __str__(self):
        return self.customer_name


