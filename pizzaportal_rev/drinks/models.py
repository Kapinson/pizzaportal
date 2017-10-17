from django.db import models

# Create your models here.

class Drink(models.Model):
    
    name = models.CharField(max_length=50)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_drink(self):
        self.save()

    def __str__(self):
        return "Drink: {}".format(self.name)
