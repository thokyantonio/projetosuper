from django.shortcuts import render
from .models import Artigo
# Create your views here.
def artigo_list(request):
    artigos= Artigo.objects.all()

    context ={
        'artigo_list':artigos,

    }
    return render(request,'artigos/artigo_list.html',context)
