from django import template

from rapidpro_community_portal.config import settings

register = template.Library()


@register.inclusion_tag('matomo.html')
def matomo():
    breakpoint()
    return {
        'site_tracker': settings.MATOMO_SITE_TRACKER,
        'site_id': str(settings.MATOMO_SITE_ID),
    }
