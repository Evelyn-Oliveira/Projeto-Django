from django.shortcuts import render, redirect
from ..models import Area, Trabalho, Professor, EscolhaProf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..forms import SaveNotasModelForm

@login_required(login_url='/login')

def confirmchoices(request):
    return render(request,'jobschoices/confirmchoices.html')