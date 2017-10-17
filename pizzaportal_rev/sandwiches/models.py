from django.db import models

# Create your models here.

class Sandwich(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_sandwich(self):
        self.save()

    def __str__(self):
        return "Sandwich: {}".format(self.name)