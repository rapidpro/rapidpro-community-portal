from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm as BasePasswordResetForm
from django.utils.translation import ugettext_lazy as _

from wagtail.users import forms as wagtailuser_forms


class UserCreationForm(wagtailuser_forms.UserCreationForm):
    """
    Custom Form to allow for custom users with username as email. Mitigates:

    https://github.com/torchbox/wagtail/issues/158
    """
    username = forms.EmailField(required=True, label=_("Username: email"))

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class UserEditForm(wagtailuser_forms.UserEditForm):
    """
    Custom Form to allow for custom users with username as email. Mitigates:

    https://github.com/torchbox/wagtail/issues/158
    """
    username = forms.EmailField(required=True, label=_("Username: email"))

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)


class PasswordResetForm(BasePasswordResetForm):

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        Override of Django default method since our email field IS the username.
        """
        active_users = get_user_model()._default_manager.filter(
            username__iexact=email, is_active=True)
        return (u for u in active_users if u.has_usable_password())
