from time import time
from turtle import distance
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

    @classmethod
    def calculate_fares(cls,time,distance):
        '''
        This method is used to calculate the fare based on the time and distance.
        :param time:
        :param distance:
        :return:
        '''
        '''get the fare data from the DB'''
        fare_data=cls.objects.get(time=time)
        '''get the service charge,surge charge,initial fare and kilometer charge from the DB'''
        service_charge=fare_data.service_charge 
        surge_charge=fare_data.surge_charge
        initial_fare=fare_data.initial_fare
        kilometer_charge=fare_data.kilometer_charge
        '''calculate the fare'''
        if service_charge and surge_charge ==0:
            fare=initial_fare+distance*kilometer_charge

        elif service_charge == 0:
            ifare=initial_fare+distance*kilometer_charge
            '''fare =surge percentage of ifare'''
            fare=ifare+(ifare*surge_charge)/100
        elif surge_charge == 0:
            fare=initial_fare+distance*kilometer_charge
            fare=ifare+(ifare*service_charge)/100
        else:  
            ifare=initial_fare+distance*kilometer_charge
            
            fare=ifare+(ifare*surge_charge)/100+(ifare*service_charge)/100

        return fare   


class Inputs(models.Model):
    time=models.TimeField()
    distance=models.FloatField(max_length=200)

    