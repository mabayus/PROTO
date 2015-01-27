'''
Created on 17 juin 2014

@author: georges
'''
from django import forms
from Proto1.settings import BASE_DIR
from django.db import models

class Upload_algo(forms.Form):
    '''    classdocs    '''
    nom  = forms.CharField(max_length = 50)
    file = models.FileField()    