from django.shortcuts import render, redirect
from ..models import Area, Trabalho, Professor, EscolhaProf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms import SaveNotasModelForm

@login_required(login_url='/login')

def sendresults(request, id=None):

    login_usuario = request.user
    prof = Professor.objects.filter(nome=login_usuario).first()
    trabescolhidos = EscolhaProf.objects.filter(professor_id=prof.id)
    tamanho = len(trabescolhidos)
    context  = {
            'trabescolhidos':trabescolhidos,
            'tamanho': tamanho,
    }
  
    if request.method == 'GET':
         return render(request, 'jobschoices/showchoicejobs.html', context=context)
    
    else:
        if(len(trabescolhidos)<10):
            areas =  Area.objects.all()
            context = {
                'some_flag':True,
                'areas':areas,
            }
            return render(request, 'index/index.html', context=context)
        
        form = SaveNotasModelForm(request.POST)
        if form.is_valid():
            i=0
            for trabs in trabescolhidos:
                trab = EscolhaProf.objects.get(id=trabs.id)
                priority = request.POST.getlist("addnota")
                print(priority)
                trab.nota=priority[i]
                trab.save()
                i=i+1 
            trabescolhidos = EscolhaProf.objects.filter(professor_id=prof.id)
            context  = {
                'trabescolhidos':trabescolhidos,
                'tamanho':tamanho,
             }
        return render(request, 'jobschoices/sendresults.html', context=context)
