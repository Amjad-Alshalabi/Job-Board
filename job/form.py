from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import apply, Job



class ApplyForm(ModelForm):

     class Meta:
        model = apply
        fields = [
        'name' ,
        'email' ,
        'website',
        'cv' ,
        'cover_letter'
        ]


class AddForm(ModelForm):
   class Meta:
      model = Job
      fields = '__all__'
      exclude = ['owner', 'slug']      