'''
Created on 23 juin 2014

@author: georges
'''
from django.shortcuts import render


def discribe_probleme(request):
    code = "first"
    if request.method == 'POST':
       if (request.POST['describe'] != None) and (request.POST['code'] != None):
        code = request.POST['code']
        valeur = request.POST['describe']
        if(code  == "1"):
            return render(request,'Proto1/vue/editeur.html',{'message':"évaluation code : \n"+valeur}) 
        elif(code  == "2"):
            return render(request,'Proto1/vue/editeur.html',{'message':"exécution code : \n"+valeur})
           #code source à modifier inclure le comportement de la page dans chaque cas                                            
    return render(request,'Proto1/vue/editeur.html',{'message':"vide pour le moment "+code})