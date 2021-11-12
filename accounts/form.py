from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from .models import Profile



class SignupForm(UserCreationForm):
    class Meta:
      model = User
      fields =['username', 'email', 'password1', 'password2']
    #   exclude = ['owner', 'slug']      


class UserForm(ModelForm):
  class Meta:
    model = User
    fields =['first_name', 'last_name', 'email']

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['phone_number', 'image']