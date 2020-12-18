from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your title'
            }
        )
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your description'
            }
        )
    )

    featured = forms.BooleanField(required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'placeholder': 'Your description'
            }
        )
    )

    class Meta:
        model = Product
        fields = '__all__'

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get('title')
    #     print('title:', title)
    #     if not 'abc' in title:
    #         raise forms.ValidationError("Title is not a valid")
    #     return title
