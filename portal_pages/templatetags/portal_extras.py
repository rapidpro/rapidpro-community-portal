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

@register.inclusion_tag('portal_pages/tags/filter_list.html', takes_context=True)
def display_filter_list(context, filter_type, tags_header, items, request_list):

    context.request.tags_header = tags_header # ie. countries
    context.request.tags_header_title = tags_header.title() # ie. countries
    
    request_vars = context.request.GET.get(filter_type,"")

    search_query = ""
    if context.request.POST.get("search", ""):
        search_query =  "&search=" + context.request.POST.get("search", "")
    elif context.request.GET.get("search", ""):
        search_query = "&search=" + context.request.GET.get("search", "")

    addl_filters_string = ""
    for request_item in request_list.split(","):
        addl_filters_string = addl_filters_string + "&" + request_item + "=" + context.request.GET.get(request_item, "")

    if request_vars: # ie. Afghanistan,China
        context.request.collapse_state = "uncollapsed"
    else:
        context.request.collapse_state = "collapsed"

    context.request.link_items = []
    for item in items:
        if item.name in request_vars:
            item_class = "active"
            # Remove this active item in the list to toggle filter off
            request_vars_list = request_vars.lstrip(",").split(",") # Strip out any leading comma
            request_vars_list.remove(item.name)
            item_href="?" + filter_type + "=" + ",".join(request_vars_list)
        else:
            item_class = ""
            request_vars_string = (request_vars + "," + item.name).lstrip(",") # Strip out any leading comma
            item_href="?" + filter_type + "=" + request_vars_string

        # Append the search query to the string
        if search_query:
            item_href = item_href + search_query

        # Append all the other filter variables to the URL string
        if addl_filters_string:
            item_href = item_href + addl_filters_string


        context.request.link_items.append({"class": item_class, "href": item_href, "name": item.name})
    
    return {
        'request': context['request'],
    }

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
