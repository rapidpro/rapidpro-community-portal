from django import template

register = template.Library()

@register.filter
def make_unique(value, unique_var): # Only one argument.
    """Converts a string into all lowercase"""
    return value.distinct(unique_var).order_by(unique_var)