from django.forms import ModelForm

from .models import MarketplaceEntryPage

class MarketplaceEntryForm(ModelForm):

    class Meta:
        model = MarketplaceEntryPage
        fields = [  'title', 'biography', 'date_start', 'telephone',
                    'email', 'address_1', 'address_2', 'city',
                    'state', 'country', 'post_code', 'website' ]
