from django.shortcuts import render
from django.shortcuts import render
from Proto1.settings import BASE_DIR
from language.grammaire import parseInput, init_var
from _csv import Error
#from language.grammaire import *
# Create your views here.

def discribe_probleme(request):
    code = "first"
    '''if(request.session.get('login',True)):
           return render(request,'Proto1/vue/index.html',{'message':"Merci de vous authentifier"})'''
    if (request.method == 'POST'):
       #verification de l'authentification'       
       if (request.POST['describe'] != None) and (request.POST['code'] != None):
        code = request.POST['code']
     #   valeur = parseInput(request.POST['describe'])
        #file = open(BASE_DIR+"/language/texte.txt","w")
        #file.write(request.POST['describe'])
        #file.close()
        init_var()
        valeur = "une faute"
        try :
            #content = open(BASE_DIR+"/language/texte.txt","r").read()
            
            editeur = request.POST['describe']
            print(editeur)
            valeur =parseInput(editeur)             
            if(not isinstance(valeur, Exception)):
                print ("J'ai traillé")
                if (valeur[0] == 1):           
                    if(code  == "1"):
                        return render(request,'Proto1/vue/description.html',{'message':"évaluation code : \n"+str(valeur[1]),'editeur':editeur}) 
                    elif(code  == "2"):
                        return render(request,'Proto1/vue/description.html',{'message':"exécution code : \n"+str(valeur[1]),'editeur':editeur})
                elif (valeur[0] == 0):
                     return render(request,'Proto1/vue/description.html',{'message':"Compiled successfull !!!\n",'editeur':editeur})
            else :
                return render(request,'Proto1/vue/description.html',{'message':"une erreur est survenue lors de la compilation %s \n" %(valeur),'editeur':editeur})
        except Error  :
           print( "une erreur")
        
            
           #code source à modifier inclure le comportement de la page dans chaque cas                                            
    return render(request,'Proto1/vue/description.html',{'message':"vide pour le moment ",'editeur':"votre description ici",'workspace':""})



