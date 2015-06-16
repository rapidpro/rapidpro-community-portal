from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailsearch.urls import frontend as wagtailsearch_frontend_urls

from portal_pages import views

from accounts import urls as accounts_urls

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),
    # Overwrite wagtail hooks url registration for user URLs
    # https://github.com/torchbox/wagtail/issues/158
    url(r'^admin/users/', include(accounts_urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^search/', include(wagtailsearch_frontend_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^add-marketplace/', views.get_marketplace_entry, name='get_marketplace'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
