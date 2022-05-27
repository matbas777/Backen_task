from django.db import models

# Create your models here.



class Item(models.Model):
    name = models.CharField(max_length=70)
    price_pln = models.DecimalField(max_digits=7, decimal_places=2)
    price_usd = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    proce_eur= models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)


class Zombie(models.Model):
    name = models.CharField(max_length=70)
    creata_date = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Item, null=True, blank=True, on_delete=models.CASCADE)