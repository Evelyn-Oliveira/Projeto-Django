from django.shortcuts import render, redirect
from ..models import Area, Trabalho, Professor, EscolhaProf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login')


def showchoicejobs(request, id=None):
    login_usuario = request.user
    prof = Professor.objects.filter(nome=login_usuario).first()
    trabescolhidos = EscolhaProf.objects.filter(professor_id=prof.id)
    tamanho = (len(trabescolhidos))
    context  = {
            'trabescolhidos':trabescolhidos,
            'tamanho':tamanho,
    }
    print(context)
    if request.method == 'POST':
    
        return render(request, 'jobschoices/showchoicejobs.html', context=context)
    
    else:
        if id != None:
            trabescolhidos = EscolhaProf.objects.get(id=id).delete()
            trabescolhidos = EscolhaProf.objects.filter(professor_id=prof.id)
            tamanho = (len(trabescolhidos))
            context  = {
                'trabescolhidos':trabescolhidos,
                'tamanho':tamanho,
            }
            
        return render(request, 'jobschoices/showchoicejobs.html', context=context)

