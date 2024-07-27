from django import forms
from .models import contactus, order_emails




class UserForm(forms.ModelForm):
      class Meta:
        model = contactus
        fields = '__all__'

class emailform(forms.ModelForm):
    class Meta:
        model = order_emails
        fields = '__all__'
  
