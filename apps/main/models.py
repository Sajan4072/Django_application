from django.db import models

# Create your models here.

'''I have created this model incase if the fare charges are likely to change in the future so instead of changing the view's logic we cam simply change the fare data in DB.'''
class Fare(models.Model):
    time=models.TimeField(primary_key=True,auto_now=False,auto_now_add=False)
    service_charge = models.FloatField(max_length= 100)
    surge_charge = models.FloatField(max_length= 100)
    initial_fare = models.FloatField(max_length= 100)
    kilometer_charge = models.FloatField(max_length= 100)

    def __str__(self):
        return f"{self.time}-{self.service_charge}-{self.surge_charge}-{self.initial_fare}-{self.kilometer_charge}"

    class Meta:
        db_table = 'fare'
        verbose_name = 'Fare'
        verbose_name_plural = 'Fares'
