from django.shortcuts import render
from model.algorithmes import handle_uploaded_file
from upload_algo.form import DocumentForm
from upload_algo.models import Document
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def upload_file(request):    
    if request.method == 'POST':        
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['fichier'])
            newdoc.save()
            return render(request,'Proto1/vue/upload_algo.html',{'message':"upload complet  !!!"})
        else :
            render(request,'Proto1/vue/upload_algo.html',{'message':"tous les champs doivent être remplis !!!"})                                    
    return render(request,'Proto1/vue/upload_algo.html',{'message':"vide pour le moment"})