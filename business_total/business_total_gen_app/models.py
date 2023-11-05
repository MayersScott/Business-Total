from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    cost_price = models.FloatField()
    selling_price = models.FloatField()
    kol_d = models.FloatField()
    supplier_url = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return self.name
