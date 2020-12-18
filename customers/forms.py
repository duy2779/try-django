from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your phone'
            }
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your email'
            }
        )
    )


    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
