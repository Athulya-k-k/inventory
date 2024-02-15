# inventory/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)  # Add this field for stock quantity

    def __str__(self):
        return self.name

    def record_sale(self, quantity_sold):
        if self.quantity >= quantity_sold:
            self.quantity -= quantity_sold
            self.save()
            return True
        else:
            return False
        
# inventory/models.py
class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    sale_date = models.DateTimeField(auto_now_add=True)

