from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f' {self.title} : {self.price}'
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    BookingDate = models.DateTimeField()
    No_of_guests = models.IntegerField()

    def __str__(self):
        return self.name
