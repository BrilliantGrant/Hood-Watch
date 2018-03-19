from django import forms
from . models import Neighborhood,Business,Profile
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm): 
    
    class Meta:
        model = Profile
        fields = ['name','email']


class BusinessForm(forms.ModelForm): 
    
    class Meta:
        model = Business
        fields = ['business_name','business_email']



