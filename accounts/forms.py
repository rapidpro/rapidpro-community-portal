from django import forms
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailusers import forms as wagtailuser_forms


class UserCreationForm(wagtailuser_forms.UserCreationForm):
    """
    Custom Form to allow for custom users with username as email. Mitigates:

    https://github.com/torchbox/wagtail/issues/158
    """
    username = forms.EmailField(required=True, label=_("Email"))

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        del self.fields['email']


class UserEditForm(wagtailuser_forms.UserEditForm):
    """
    Custom Form to allow for custom users with username as email. Mitigates:

    https://github.com/torchbox/wagtail/issues/158
    """
    username = forms.EmailField(required=True, label=_("Email"))

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        del self.fields['email']
