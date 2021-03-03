from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Marage
# from django_countries.widgets import CountrySelectWidget
# from Marage_Bureau.models import Country,State,City


class MarageRegisteration(forms.ModelForm):
    # country = forms.ModelChoiceField(queryset=Country.objects.all())
    # state = forms.CharField(required=False)
    city = forms.CharField(required=False)
    profile_pic = forms.ImageField()
    house_bill_address_pic = forms.ImageField(required = True)
    cnic_front_pic = forms.ImageField(required = True)
    cnic_back_pic = forms.ImageField(required = True)
    address = forms.CharField( required =True, widget=forms.Textarea(attrs={"cols":90, "rows":2}))
    anything_else = forms.CharField(required = False, widget=forms.Textarea(attrs={"cols":60, "rows":2}))
    class Meta:
        model = Marage
        fields = '__all__'
        widgets = {
            'age': forms.Select(attrs={'class':'form-control'}),
            'caste': forms.Select(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'height': forms.Select(attrs={'class':'form-control'}),
            'profession': forms.Select(attrs={'class':'form-control'}),
            'gardian_profession': forms.Select(attrs={'class':'form-control'}),
            'siblings': forms.Select(attrs={'class':'form-control'}),
            'married_brothers': forms.Select(attrs={'class':'form-control'}),
            'married_sisters': forms.Select(attrs={'class':'form-control'}),
            'marrage_times': forms.Select(attrs={'class':'form-control'}),
            'referance': forms.TextInput(attrs={'class':'form-control'}),
            'referance_person_detail': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control', 'id':'country'}),
            'state': forms.Select(attrs={'class':'form-control', 'id':'states'}),
            'city': forms.Select(attrs={'class':'form-control', 'id':'city'}),
            'is_approved': forms.Select(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_id_link': forms.TextInput(attrs={'class':'form-control'}),
            }
        
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']