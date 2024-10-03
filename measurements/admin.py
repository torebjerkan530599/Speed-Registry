from django.contrib import admin
from .models import Measurements

# Register your models here.
class MeasurementAdmin(admin.ModelAdmin):
  list_display = ("id", "licence_plate", "date_time_a", "date_time_b", "avg_speed", "make", "car_image")

admin.site.register(Measurements,MeasurementAdmin)