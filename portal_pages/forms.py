from datetime import datetime

from django.forms import ModelForm, widgets

from wagtail.wagtailimages.models import Image

from .models import MarketplaceEntryPage, BlogPage

class MarketplaceEntryForm(ModelForm):

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

class BlogForm(ModelForm):

    required_css_class = 'required'

    class Meta:
        model = BlogPage
        labels = {
            'date': 'Blog Date'
        }
        fields = [
            'title', 'body', 'date'
        ]
        widgets = {
            'date': widgets.DateInput(attrs={'class': 'datepicker'})
        }