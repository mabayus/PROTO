from django.shortcuts import render
from inscription.models import verifie_login_existe,\
    creer_utilisateur
import os
from Proto1.settings import BASE_DIR

# Create your views here.
def incription(request):    
    if request.method == 'POST': 
        print("inscription !!! \n")        
        if ((request.POST['login'] != None) and (request.POST['pwd'] != None)) :
            if ((request.POST['login'] != "") and (request.POST['pwd'] != "")) : 
               login = request.POST['login']
               password = request.POST['pwd']
               name = request.POST['name']
               firstname = request.POST['firstname']
               profil = request.POST['profil']
               doublon = verifie_login_existe(login)
               if( not doublon ):
                   chemin_espace_perso = BASE_DIR+"/Workspace/"+login
                   chemin_relatif = "/Workspace/"+login                   
                   msg_bd = creer_utilisateur(login,password,name,firstname,profil,chemin_relatif)
                   print(" message de la base de donées : %s \n" %msg_bd)
                   if(msg_bd == "OK"):
                       os.system("mkdir "+chemin_espace_perso+"; chmod 777 "+chemin_espace_perso)
                       return render(request,'Proto1/vue/index.html',{'message':"vous pouvez maintenant vous connecter"})
                   else:
                       return render(request,'Proto1/vue/inscription.html',{'message':"Un problème est survenu lors de votre enregistrement"})
               else : 
                   return render(request,'Proto1/vue/inscription.html',{'message':" le login "+login+" est déja utilisé"})       
            else :
                   return render(request,'Proto1/vue/inscription.html',{'message':"tous les champs doivent être remplis !!!"})                                    
    return render(request,'Proto1/vue/inscription.html',{'message':"Entrez vos informations"})