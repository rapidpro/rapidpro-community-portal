from django import template
from ..models import DefaultTopImage

register = template.Library()

@register.filter
def make_unique(value, unique_var): # Only one argument.
    """Make the queryset unique by unique_var, sort by unique_var"""
    if hasattr(value, "distinct"): # Need to check so that this does not break in Preview mode in Wagtail
        return value.distinct(unique_var).order_by(unique_var)
    else:
        return value

@register.filter
def remove_from_string(value, value_to_remove): 
    """Remove a value from a list of values, ie. in order to unselect a Country from a filter of Countries"""
    if value.find("," + value_to_remove) >= 0:
        value = value.replace("," + value_to_remove, "")
    elif value.find(value_to_remove) >= 0:
        value = value.replace(value_to_remove, "")

    return value


@register.assignment_tag
def randomize_image(page):
    if page.top_image:
        top_image = page.top_image
    else:
        try:
            top_image = DefaultTopImage.objects.order_by("?")[0].default_top_image
        except IndexError:
            top_image = ""

    return top_image
