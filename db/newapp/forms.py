from django import forms
from .models import Person

class userForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']
