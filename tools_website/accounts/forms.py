from django import forms
from .models import contactus, order_emails




class userform(forms.ModelForm):
    
    class Meta:
        model = contactus
        fields = ['Username', 'Your_trc20_wallet_address']

class emailform(forms.Form):
    Email = forms.EmailField(label="Email Address", max_length=100)
