from django import forms
from app_seven.models import User
class NewUser(forms.ModelForm):
    class Meta():
        model=User
        fields="__all__"
