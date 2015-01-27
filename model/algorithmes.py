'''
Created on 18 juin 2014

@author: georges
'''
from Proto1.settings import BASE_DIR

def handle_uploaded_file(f,name):
    with open(name+".rar", 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)