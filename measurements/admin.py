from django.contrib import admin
from .models import Measurements
from django.utils.html import format_html

# Register your models here.
class MeasurementAdmin(admin.ModelAdmin):
  list_display = ("id", "licence_plate", "date_time_a", "date_time_b", "avg_speed", "make", "car_image")
  
  # def car_image_display(self, obj):
  #   if obj.car_image:
  #     return format_html('<img src="{}" width="100" />', obj.car_image.url)
  #   return "No Image"
    
  # car_image_display.short_description = "Car Image"

admin.site.register(Measurements,MeasurementAdmin)