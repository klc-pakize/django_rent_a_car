from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):

    GEAR = (
        ('a', 'automatic'),
        ('m', 'manuel')
    )

    plate_number = models.CharField(max_length = 15, unique = True)
    brand = models.CharField(max_length = 15)
    model = models.CharField(max_length = 20)
    rent_per_day = models.DecimalField(
        max_digits = 6,  # max_digits = We specify how many digits the number will have at most.
        decimal_places = 2,  # decimal_places = We specify the maximum number of digits after the comma.
        validators = [MinValueValidator(50)],  # MinValueValidator = We specify the minimum number to be entered in this field, not less than the number we specified.
    )
    gear = models.CharField(max_length = 1, choices = GEAR)
    year = models.SmallIntegerField()
    availability = models.BooleanField(default = True)

    def __str__(self):
        return f" {self.plate_number} {self.model} {self.brand} "
    

class Reservation(models.Model):

    customer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'customers')
    car = models.ForeignKey(Car, on_delete = models.CASCADE, related_name = 'cars')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.customer} {self.car}"
    
    #! A user can only book one car on the same dates:

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['customer', 'start_date', 'end_date'], name = 'user_rent_date'
            )
        ]