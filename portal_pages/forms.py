from django import forms
from django.forms import ModelForm
from django.template.loader import render_to_string

from wagtail.wagtailimages.models import Image

from .models import MarketplaceEntryPage

class HoneyForm(forms.Form):
    '''
        Form containing a quick implementation of validation code that attempts
        to thwart spam.

        Field names in this form are composed by joining together common
        form field names. This results in field names that aren't used in
        practice. Note that these field names do not reflect the
        actual use of the fields.

        email_field_email - Honeypot field. Must be left blank to be valid.
                            Hidden from the user.
        company_company_email - JS-filled captcha.
                                Must not be blank upon submission.
                                Hidden from the user.
    '''

    # STATIC FOR NOW. TODO: Make this dynamic.
    HONEY_FIELD_LABEL = "Leave this empty"
    HUMANITY_TEST_LABEL = "What is four plus five?"
    HUMANITY_TEST_VALUE = "nine"

    email_field_email = forms.CharField(label=HONEY_FIELD_LABEL, required=False)
    company_company_email = forms.CharField(label=HUMANITY_TEST_LABEL, required=False)

    def clean_email_field_email(self):
        email_field_email = self.cleaned_data.get("email_field_email")
        if email_field_email:  # not blank
            raise forms.ValidationError("Invalid value")
        return email_field_email

    def clean_company_company_email(self):
        company_company_email = self.cleaned_data["company_company_email"]
        if company_company_email.lower() != HoneyForm.HUMANITY_TEST_VALUE:
            raise forms.ValidationError("Incorrect answer")
        return company_company_email


class SpamProtectedForm(forms.Form):
    # NOTE: {{ form.media }} must be rendered in the template for this form,
    # AFTER inclusion of jquery as spambuster.js requires jquery. So template
    # for a page this is used on should utilize extra-js block to get this
    # javascript (and jquery if jquery is not available site-wide) included
    # on the page.
    class Media:
        js = ("js/spambuster.js",)

    HONEYPOT_CSS_CLASS = "topyenoh"

    def __init__(self, *args, **kwargs):
        super(SpamProtectedForm, self).__init__(*args, **kwargs)
        self.honeypot_form = HoneyForm(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if not self.honeypot_form.is_valid():
            raise forms.ValidationError("Invalid submission")
        return super(SpamProtectedForm, self).clean(*args, **kwargs)

    @property
    def honeypot(self):
        return render_to_string('util/spambuster/honeypot.html', {
            'form': self
        })


class MarketplaceEntryForm(SpamProtectedForm, ModelForm):

    required_css_class = 'required'

    class Meta:
        model = MarketplaceEntryPage
        labels = {
            'title': 'Company Name',
            'post_code': 'Post/Zip Code'
        }
        fields = [
            'title', 'biography', 'date_start', 'telephone',
            'email', 'address_1', 'address_2', 'city',
            'state', 'country', 'post_code', 'website'
        ]

class ImageForm(ModelForm):

    class Meta:
        model = Image
        labels = {
            'file': 'Logo Image File'
        }
        fields = [
            'file'
        ]
