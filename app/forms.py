from dataclasses import fields
from pyexpat import model
from django import forms

from app.models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpages
        fields='__all__'

class RecordsForm(forms.ModelForm):
    class Meta:
        model=Access_Records
        fields='__all__'
