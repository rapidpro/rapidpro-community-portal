from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as django_auth_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from accounts import forms as accounts_forms, urls as accounts_urls

# from wagtail.search.urls import frontend as wagtailsearch_frontend_urls


urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    # Overwrite wagtail hooks url registration for user URLs
    # https://github.com/torchbox/wagtail/issues/158
    url(r'^admin/users/', include(accounts_urls)),
    # Overwrite wagtail admin password reset view as well
    url(r'^admin/password_reset/$', django_auth_views.PasswordResetView.as_view(), {
        'template_name': 'wagtailadmin/account/password_reset/form.html',
        'email_template_name': 'wagtailadmin/account/password_reset/email.txt',
        'subject_template_name': 'wagtailadmin/account/password_reset/email_subject.txt',
        'password_reset_form': accounts_forms.PasswordResetForm,
        'post_reset_redirect': 'wagtailadmin_password_reset_done',
    }, name='wagtailadmin_password_reset'
    ),
    url(r'^admin/', include(wagtailadmin_urls)),
    # url(r'^search/', include(wagtailsearch_frontend_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's serving mechanism
    url(r'', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += url(r'^__debug__/', include(debug_toolbar.urls)),
