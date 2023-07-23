from django.db import models


# Create your models here.
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    booking_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=10)

    def __str__(self): 
        return self.name

class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.IntegerField(null=False) 
   inventory = models.IntegerField()

   def __str__(self):
      return f'{self.title} : {str(self.price)}'