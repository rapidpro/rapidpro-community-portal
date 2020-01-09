from django import template

from ..models import DefaultTopImage

register = template.Library()


@register.filter
def make_unique(qs, unique_var):
    """Make the queryset unique by unique_var, sort by unique_var"""
    if hasattr(qs, "distinct"):  # Need to check so that this does not break in Preview mode in Wagtail
        distinct_pks = qs.distinct(unique_var).order_by(unique_var).values_list('pk', flat=True)
        return qs.filter(pk__in=distinct_pks)
    else:
        return qs


@register.filter
def url_param_dict_to_list(url_items_dict):
    """Turn this dictionary into a param list for the URL"""
    params_list = ""
    for key, value in url_items_dict:
        if key != "page":
            params_list += "&%s=%s" % (key, value)

    return params_list


@register.filter
def remove_from_string(value, value_to_remove):
    """Remove a value from a list of values, ie. in order to unselect a Country from a filter of Countries"""
    if value.find("," + value_to_remove) >= 0:
        value = value.replace("," + value_to_remove, "")
    elif value.find(value_to_remove) >= 0:
        value = value.replace(value_to_remove, "")

    return value


@register.filter
def add_spacing(value):
    return value.replace(">", "> ")


@register.inclusion_tag('portal_pages/tags/filter_list.html', takes_context=True)
def display_filter_list(context, items, request_list):
    request = context['request']
    filter_type = items.model._meta.verbose_name.replace(' ', '_')
    request_vars = request.GET.get(filter_type, "")
    search_q = request.GET.get("search", "")
    search_query = "&search=" + search_q if search_q else ""

    addl_filters_string = ""
    for request_item in request_list.split(","):
        addl_filters_string = addl_filters_string + "&" + request_item + "=" + request.GET.get(request_item, "")

    # Collapse the div if no filters are currently active for this filter
    collapse_state = "uncollapsed" if request_vars else "collapsed"

    link_items = []
    for item in items:
        if item.name in request_vars.split(","):
            item_class = "active"
            # Remove this active item in the list to toggle filter off
            request_vars_list = request_vars.lstrip(",").split(",")  # Strip out any leading comma
            request_vars_list.remove(item.name)
            item_href = "?" + filter_type + "=" + ",".join(request_vars_list)
        else:
            item_class = ""
            request_vars_string = (request_vars + "," + item.name).lstrip(",")  # Strip out any leading comma
            item_href = "?" + filter_type + "=" + request_vars_string

        # Append the search query to the string
        if search_query:
            item_href = item_href + search_query

        # Append all the other filter variables to the URL string
        if addl_filters_string:
            item_href = item_href + addl_filters_string

        link_items.append({"class": item_class, "href": item_href, "name": item.name})

    plural_item_name = items.model._meta.verbose_name_plural
    return {
        'tags_header': plural_item_name.replace(' ', '-'),
        'tags_header_title': plural_item_name.title(),
        'collapse_state': collapse_state,
        'link_items': link_items,
    }


@register.simple_tag()
def randomize_image(page):
    if page and page.top_image:
        top_image = page.top_image
    else:
        try:
            top_image = DefaultTopImage.objects.order_by("?")[0].default_top_image
        except IndexError:
            top_image = ""

    return top_image
