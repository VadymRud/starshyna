from django import template
from staff.models import Staff
register = template.Library()

@register.simple_tag
def get(value):

    try:
        name = Staff.objects.filter(company=value)
    except Staff.DoesNotExist:
        name = 'vacant'
   
    return name

# register.filter('get', get)