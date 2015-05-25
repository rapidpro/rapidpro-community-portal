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

@register.inclusion_tag("base.html")
def randomize_image():
    top_image_random = DefaultTopImage.objects.order_by("?")[0]
    return {"top_image_random": top_image_random}
