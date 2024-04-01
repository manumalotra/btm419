from django import template
from datetime import timedelta

register = template.Library()

@register.filter(name='add_days')
def add_days(value, days):
    return value + timedelta(days=days)