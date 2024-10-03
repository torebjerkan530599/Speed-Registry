from django.db import models

# Create your models here.


class Measurements(models.Model):
    licence_plate = models.CharField(max_length=255)
    date_time_a = models.DateTimeField(null=True, blank=True)
    date_time_b = models.DateTimeField(null=True, blank=True)
    avg_speed = models.FloatField(null=True)
    make = models.CharField(null=True, max_length=255)
    car_image = models.ImageField(upload_to='car_images/', null = True, blank = True)
    
    def __str__(self):
        time_a_str = self.date_time_a.strftime("%H:%M:%S") if self.date_time_a else "None"
        time_b_str = self.date_time_b.strftime("%H:%M:%S") if self.date_time_b else "None"
        return f"{self.licence_plate} {time_a_str}  {time_b_str} {self.avg_speed} {self.make}"