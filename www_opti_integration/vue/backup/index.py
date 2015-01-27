'''
Created on 5 juin 2014

@author: georges
'''
from django.core.context_processors import request
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from model.utilsateur import testConnexion
#from vue.upload import Upload_algo
from model.algorithmes import handle_uploaded_file
from vue.backup.upload import Upload_algo


def acceuil(request):
    form = Upload_algo()
    if request.method == 'POST':         
        if ((request.POST['login'] != None) and (request.POST['password'] != None)) : 
            if(testConnexion(request.POST['login'],request.POST['password'])):
                
                return render(request,'Proto1/vue/upload_algo.html',{'message':"salut " + request.POST['login'],'form':form},context_instance=RequestContext(request))
            
            else:
                return render(request,'Proto1/vue/authentification.html',{'message':"login ou mot de passe incorrect"})  
        else :
               render(request,'Proto1/vue/authentification.html',{'message':"tous les champs doivent être remplis !!!"})                                    
    return render(request,'Proto1/vue/authentification.html',{'message':"Merci de vous authentifier"})

def login(request):
    return render_to_response('Proto1/vue/auth.py',{})
    
    
    
def upload(request):
    form = Upload_algo()
    if request.method == 'POST':
        form = Upload_algo(request.POST,request.FILES) 
        if (form.is_valid()) : 
            handle_uploaded_file(request.FILES['file'],request.POST['nom'])
            return render(request,'Proto1/vue/vide.html',{'message':"upload complet  !!!"},context_instance=RequestContext(request))
        else :
               render(request,'Proto1/vue/upload_algo.html',{'message':"tous les champs doivent être remplis !!!"})                                    
    return render(request,'Proto1/vue/upload_algo.html',{'message':"vide pour le moment",'form':form})



