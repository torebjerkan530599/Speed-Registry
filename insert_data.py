import os
import sys
import django
from pathlib import Path
from datetime import datetime


SPEED_LIMIT = 60
DISTANCE = 5000 # meters between laser measurements
MARGIN_OF_ERROR = 0.05

# Add project root to Python path
#sys.path.append(Path(__file__).resolve().parent.parent.parent)
#print(Path(__file__).resolve().parent.parent)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'traffic_control.settings')
django.setup()

from measurements.models import Measurements

def fileToDictionary(txt_file) -> dict:
    try:
        path = Path(__file__).parent / txt_file # reading from the text file in the directory code is run from
        content = path.read_text(encoding="utf-8")
        return {key: value for line in content.splitlines() for key, value in [line.strip().split(', ')]}
    except FileNotFoundError:
        print('file not found')


def insert_passings():
    a_dict = fileToDictionary('box_a.txt')
    b_dict = fileToDictionary('box_b.txt')
    
    for licence_plate in a_dict:
            if licence_plate in b_dict: # check if the car reached box_b
                datetime_object_a = datetime.strptime(a_dict[licence_plate], '%Y-%m-%d %H:%M:%S') #string to datetime object
                #time_only_a = datetime_object_a.strftime("%H:%M:%S")
                datetime_object_b = datetime.strptime(b_dict[licence_plate], '%Y-%m-%d %H:%M:%S')
                #time_only_b = datetime_object_b.strftime("%H:%M:%S")
                duration = datetime_object_b - datetime_object_a
                speed = (DISTANCE / duration.total_seconds()) * 3.6 # m/s to km/h

                print(f"Parsed datetime A: {datetime_object_a}")
                print(f"Parsed datetime B: {datetime_object_b}")
                
                
                new_record = Measurements(
                    licence_plate=licence_plate, 
                    date_time_a= datetime_object_a, 
                    date_time_b= datetime_object_b,
                    avg_speed = speed)

                
                new_record.save()

FILE_PATH = Path(__file__).parent / 'vehicle_types.txt'

def read_models():
    with FILE_PATH.open(mode='r', encoding= ' utf-8') as file:
        content = file.read()
        vehicle_models = [line for line in content.splitlines()]
    return vehicle_models


def insert_vehicle_types():
    measurements = Measurements.objects.all()
    vehicle_models = read_models()
    
    for measurement, vehicle_model in zip(measurements, vehicle_models):
        measurement.make = vehicle_model
        measurement.save()
    

#insert_passings()
insert_vehicle_types()
print("Data inserted successfully.")