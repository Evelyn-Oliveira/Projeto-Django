from django.shortcuts import render
from django.http import HttpResponse
from ..models import Area, Trabalho, Professor, SubArea
from django.db import models
import csv
import pandas as pd
import time


def refresh_bd():
    Trabalho.objects.all().delete()
    Area.objects.all().delete()
    Professor.objects.all().delete()
    SubArea.objects.all().delete()
    
    filename= 'tcc2022/DadosEntrada.csv'
    filenameProf = 'tcc2022/loginProfs.csv'
    df = pd.read_csv(filename, sep=";")
    df_area = df['Área'].unique()
    df_login_prof = pd.read_csv(filenameProf, sep=";")
  
    #CARREGA AREAS
    for arq in range (len(df_area)):
        a = Area(tema=df_area[arq])
        a.save()
    #CARREGA SUBAREAS
    for arq in range (len(df)):
        print("oi")
        area = df.loc[arq, 'Área']
        area_individualizada = Area.objects.filter(tema=area).first() 
        subarea = SubArea(area= area_individualizada ,subarea=df.loc[arq, 'SubÁrea'])
        subarea.save()
    #CARREGA TRABALHOS
    for arq in range (len(df)):
        subarea = df.loc[arq, 'SubÁrea']
        a = SubArea.objects.filter(subarea=subarea).first()
        trab = Trabalho(titulo=df.loc[arq,'Títulos'],resumo=df.loc[arq, 'Resumo'], subarea=a)
        trab.save()
    #CARREGA LOGINS
    for arqprof in range(len(df_login_prof)):
        login = df_login_prof.loc[arqprof,'Login']
        senha = df_login_prof.loc[arqprof, 'Senha']
        prof = Professor(nome=login, senha=senha)
        prof.save()
    
def refreshbd(request):

    if request.method=='GET':
 
        refresh_bd()
        return render(request,'login/login.html')
    else:

        refresh_bd()
        time.sleep(60) 
        return render(request,'login/login.html')
        