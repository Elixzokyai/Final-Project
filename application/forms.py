from django import forms
from .models import ApplicationUser


# create the user forms

class ApplicationUserForm(forms.ModelForm):
    class Meta:
        model = ApplicationUser
        fields = ('name', 'email','numberOfFollowers', 'following','SpecifyAccount', 'socialMediaLink')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'SpecifyAccount': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter account e.g X (Twitter)'}),
            'numberOfFollowers': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Enter number of Followers'}),
            'following': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Enter number of Following'}),
            'socialMediaLink': forms.URLInput( attrs={'class': 'form-control', 'placeholder': 'Enter Social Media Link'}),
        }