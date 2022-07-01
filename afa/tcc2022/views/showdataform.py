import re
from ..models import Area, Trabalho, Professor, EscolhaProf
from ..forms import AddJobs
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/login')
def showdataform(request):
    #print (request.user)
    if request.method =='GET':
        areas =  Area.objects.all()
        context  = {
            'areas':areas,
       }
        return render(request,'index/index.html',context=context)
    else:

        print(request.POST)
        nome = request.user
        prof = Professor.objects.filter(nome=nome).first()
       #print(prof.id)
        trabarea = request.POST.get('trabarea')
        print(trabarea)
        
        if(EscolhaProf.objects.filter(trabalho_id=trabarea)):
            print("oi")
            areas =  Area.objects.all()
            context  = {
                'areas':areas,
                'msg': 'O Trabalho anterior já foi adicionado!'
            }
            return render(request,'index/index.html',context=context)
        else:
            trabalho = Trabalho.objects.filter(id=int(trabarea)).first()
            print(prof.id)
            print("-------------")
            escolhaprof = EscolhaProf(professor=prof,trabalho=trabalho)
            escolhaprof.save()
            return redirect('showdataform')
        


