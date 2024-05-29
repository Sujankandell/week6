from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Thesis, Group

class UserRegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'user_type']

class ThesisForm(forms.ModelForm):
    class Meta:
        model = Thesis
        fields = ['title', 'description']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'members', 'thesis']
