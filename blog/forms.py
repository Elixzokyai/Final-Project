from django import forms
from .models import Blog
from djmoney.forms.widgets import MoneyWidget
class BlogForm(forms.ModelForm):
    TITLE_CHOICES = [
        ('', 'Select Title'),  # Placeholder
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ("linkedin", 'LinkedIn'),
        ('Youtube', 'Youtube'),
        ('Tiktok', 'Tiktok')
    ]

    title = forms.ChoiceField(
        choices=TITLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'Amount': MoneyWidget(attrs={'class': 'form-control'}),
            'Requirements': forms.Textarea(attrs={'class': 'form-control'}),
        }
