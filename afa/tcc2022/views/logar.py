from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..forms import LoginModelForm
from ..models import Professor
from django.contrib.auth import authenticate, login

def logar(request):
    if request.method=='GET':
        return render(request,'login/login.html')
    else:
        form = LoginModelForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            usuario = authenticate(request, username = cd['nome'], password = cd ['senha'])
            if usuario is not None:
                if usuario.is_active:
                    login(request, usuario)
                    return redirect('showdataform')
                else:
                    context = {'msg': "erro1"}
                    return render(request, 'login/login.html',context)
            else:
                context = {'msg': "Login/Senha inválido"}
                return render(request, 'login/login.html',context)  
        else:
            context = {'msg': "Digite seu Login e sua Senha"}
            return render(request, 'login/login.html',context)
