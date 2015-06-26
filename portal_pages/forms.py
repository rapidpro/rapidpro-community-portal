from django.forms import ModelForm

from wagtail.wagtaildocs.models import Document
from wagtail.wagtailimages.models import Image

from .models import MarketplaceEntryPage, CaseStudyPage


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


class CaseStudyForm(ModelForm):

    required_css_class = 'required'

    class Meta:
        model = CaseStudyPage
        labels = {
            'date': 'Month/Year of Case Study Initiation'
        }
        fields = [
            'title', 'summary', 'date'
        ]


class DocumentForm(ModelForm):

    class Meta:
        model = Image
        labels = {
            'file': 'Downloadable Package'
        }
        fields = [
            'file'
        ]