from django.shortcuts import render
from login.models import testConnexion

# Create your views here.
def acceuil(request):
    if request.method == 'POST':         
        if ((request.POST['login'] != None) and (request.POST['pwd'] != None)) :
            informations =  testConnexion(request.POST['login'],request.POST['pwd'])
            if(len(informations) != 0):
                for row in informations:
                    request.session['login'] = row[1]
                    request.session['firstname'] = row[4]
                    request.session['profil'] = row[5]
                    request.session['workspace'] = row[6]                
                print(informations)
                return render(request,'Proto1/vue/description.html',{'message':"salut " + request.POST['login']})            
            else:
                return render(request,'Proto1/vue/index.html',{'message':"login ou mot de passe incorrect"})  
        else :
               render(request,'Proto1/vue/index.html',{'message':"tous les champs doivent être remplis !!!"})                                    
    return render(request,'Proto1/vue/index.html',{'message':"Merci de vous authentifier"})
