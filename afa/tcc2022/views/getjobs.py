from django.shortcuts import render
from ..models import Trabalho, EscolhaProf, SubArea

def getjobs(request, id):
    trabalhos = Trabalho.objects.filter(subarea_id=id)
    print(trabalhos)
    return render(request, 'index/dropdowntrab.html', {'trabalhos': trabalhos})

def getsubarea(request, id):
    #print(id)
    subarea =SubArea.objects.filter(area_id=id)
    #print(subarea)
    return render(request, 'index/dropdown.html', {'subarea': subarea})

def getabstract(request, id):
    abstract = Trabalho.objects.get(id=id)
    return render(request, 'index/textareaabstract.html', {'abstract': abstract})


