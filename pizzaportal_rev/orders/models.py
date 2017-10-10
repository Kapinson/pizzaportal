from django.db import models
from django.utils import timezone

# Create your models here.

class Order(models.Model):
    consumables = models.CharField(max_length=1000)
    total_price = models.DecimalField(null=True,
                                      blank=True,
                                      decimal_places=2,
                                      max_digits=6,
                                      verbose_name="Cena zamówienia")
    delivery_address = models.CharField(max_length=100, verbose_name="Adres dostarczenia")
    phone_number = models.IntegerField(null=False, blank=False, verbose_name="Numer telefonu")
    accepted = models.BooleanField(null=False, default=False)
    date = models.DateTimeField(
        default=timezone.now)

    def create_order(self):
        self.save()

    def __str__(self):
        return "Order: {}".format(self.id)
