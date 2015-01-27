'''
Created on 12 juil. 2014

@author: georges
'''
from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )