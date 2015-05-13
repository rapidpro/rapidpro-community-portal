from django import template

register = template.Library()

@register.filter
def make_unique(value, unique_var): # Only one argument.
    """Make the queryset unique by unique_var, sort by unique_var"""
    if hasattr(value, "distinct"): # Need to check so that this does not break in Preview mode in Wagtail
        return value.distinct(unique_var).order_by(unique_var)
    else:
        return value