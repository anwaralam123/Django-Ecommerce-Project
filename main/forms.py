from django import forms
from .models import Rating,ShippingAddress
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Comfirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={
            'email':'Email'
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'form-control'})
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model=Rating
        fields=['name','title','review','rate']
        labels={
            'name':'Name *'
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'review':forms.Textarea(attrs={'class':'form-control'}),
            'rate':forms.NumberInput(attrs={'class':'form-control','type':'hidden'}),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model=ShippingAddress
        fields=['first_name','last_name','company_name','area_code','primary_phone','street_address','zip_code','business_address']
        labels={
            'company_name':'Company Name(optional)'
        }
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),   
            'last_name':forms.TextInput(attrs={'class':'form-control'}),   
            'company_name':forms.TextInput(attrs={'class':'form-control'}),   
            'area_code':forms.TextInput(attrs={'class':'form-control'}),   
            'primary_phone':forms.TextInput(attrs={'class':'form-control'}),   
            'street_address':forms.TextInput(attrs={'class':'form-control'}),   
            'zip_code':forms.TextInput(attrs={'class':'form-control'}),   
            'business_address':forms.CheckboxInput(attrs={'class':'form-control'}),   
        }