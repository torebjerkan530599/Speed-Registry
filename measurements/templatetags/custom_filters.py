# myapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
# def is_speed_offender(speed):
#     return speed > 60


def is_speed_offender(speed, speed_limit=60):
    """
    Checks if the speed exceeds the specified speed limit.
    Default speed limit is 60 km/h.
    """
    return int(speed) > speed_limit