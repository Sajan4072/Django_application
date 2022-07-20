from django.contrib import admin
from .models import Fare

# Register your models here.
'''obviously we can create better admin class for better UX but due to short time to complete the task I just registered the model here.'''

admin.site.register(Fare)
