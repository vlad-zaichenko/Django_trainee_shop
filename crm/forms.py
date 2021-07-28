from django import forms

class OrderForms(forms.Form):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))