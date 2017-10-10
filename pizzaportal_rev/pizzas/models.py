from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_ingredient(self):
        self.save()

    def __str__(self):
        return "Ingredient: {}".format(self.name)

class Pizza(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    toppings = models.ManyToManyField(Ingredient)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_pizza(self):
        self.save()

    def __str__(self):
        return "Pizza: {}".format(self.name)

class Appetizer(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_appertizer(self):
        self.save()

    def __str__(self):
        return "Appertizer: {}".format(self.name)

class Sandwich(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_sandwich(self):
        self.save()

    def __str__(self):
        return "Sandwich: {}".format(self.name)

class Drink(models.Model):

    name = models.CharField(max_length=50)
    price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=6)

    def add_drink(self):
        self.save()

    def __str__(self):
        return "Drink: {}".format(self.name)
