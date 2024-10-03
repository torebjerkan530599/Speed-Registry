from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import Measurements

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def measurements(request):
    # Retrieve the user-selected speed limit from the GET parameters, defaults to 60 if not provided
    speed_limit = request.GET.get('speed_limit', 60)
    try:
        speed_limit = int(speed_limit)
    except ValueError:
        speed_limit = 60  # Fallback to 60 if invalid

    # Retrieve all measurements from the database
    mymeasurements = Measurements.objects.all()

    # Prepare a list to hold the formatted data
    formatted_measurements = []

    for measurement in mymeasurements:
      # Extract and format the time portions
      time_only_a = measurement.date_time_a.strftime("%H:%M:%S") if measurement.date_time_a else None
      time_only_b = measurement.date_time_b.strftime("%H:%M:%S") if measurement.date_time_b else None
    
      # Append a dictionary with the formatted data
      formatted_measurements.append({
          'id': measurement.id,
          'licence_plate': measurement.licence_plate,
          'time_a': time_only_a,
          'time_b': time_only_b,
          'avg_speed': measurement.avg_speed
      })    
    context = {
      'mymeasurements' : formatted_measurements,
      'speed_limit': speed_limit  # Pass the speed limit to the template
    }

    return render(request, 'measurements.html', context)

def details(request, id):
    # Use get_object_or_404 to handle cases where the ID might not exist
    mymeasurement = get_object_or_404(Measurements, id=id)
    return render(request, 'details.html', {'mymeasurement': mymeasurement})

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))
