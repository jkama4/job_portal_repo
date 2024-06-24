from django import forms
from .models import Job
from typing import List

class JobForm(forms.ModelForm):
    """ A form for creating and updating Job instances. """
    class Meta:
        model = Job
        fields: List[str] = ['title', 'company_name', 'location', 'link', 'image']
