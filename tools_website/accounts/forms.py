from django import forms
from .models import contactus

class contactform(forms.ModelForm):
    
    class Meta:
        model = contactus
        fields = ['Username', 'Email', 'Your_trc20_wallet_address']
