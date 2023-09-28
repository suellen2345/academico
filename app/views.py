from django.shortcuts import render
from . models import *

def cidades(request):
    cidades = {
        'cidades': Cidades.objects.all()
    }

    return render(request, 'cidades/cidades.html', cidades)

def ocupacoes(request):
    ocupacoes = {
        'ocupacoes': Ocupacoes.objects.all()
    }

    return render(request, 'ocupacoes/ocupacoes.html', ocupacoes)

def pessoas(request):
    pessoas = {
        'pessoas': Pessoas.objects.all()
    }

    return render(request, 'pessoas/pessoas.html', pessoas)

def instituicoes(request):
    instituicoes = {
        'instituicoes': Instituicoes.objects.all()
    }

    return render(request, 'instituicoes/instituicoes.html', instituicoes)

def areas_do_saber(request):
    areas_do_saber = {
        'areas_do_saber': Areas_do_Saber.objects.all()
    }

    return render(request, 'areas_do_saber/areas_do_saber.html', areas_do_saber)

def cursos(request):
    cursos = {
        'cursos': Cursos.objects.all()
    }

    return render(request, 'cursos/cursos.html', cursos)

def periodos(request):
    periodos = {
        'periodos': Periodos.objects.all()
    }

    return render(request, 'periodos/periodos.html', periodos)

def disciplinas(request):
    diciplinas = {
        'diciplinas': Diciplinas.objects.all()
    }

    return render(request, 'disciplinas/disciplinas.html', diciplinas)

def matriculas(request):
    matriculas = {
        'matriculas': Matriculas.objects.all()
    }

    return render(request, 'matriculas/matriculas.html', matriculas)

def avaliacoes(request):
    avaliacoes = {
        'avaliacoes': Avaliacoes.objects.all()
    }

    return render(request, 'avaliacoes/avaliacoes.html', avaliacoes)

def frequencias(request):
    frequencias = {
        'frequencias': Frequencias.objects.all()
    }

    return render(request, 'frequencias/frequencias.html', frequencias)

def turmas(request):
    turmas = {
        'turmas': Turmas.objects.all()
    }

    return render(request, 'turmas/turmas.html', turmas)

def ocorrencias(request):
    ocorrencias = {
        'ocorrencias': Ocorrencias.objects.all()
    }

    return render(request, 'ocorrencias/ocorrencias.html', ocorrencias)

def disciplinas_cursos(request):
    disciplinas_cursos = {
        'disciplinas_cursos': Disciplinas_Cursos.objects.all()
    }

    return render(request, 'disciplinas_cursos/disciplinas_cursos.html', disciplinas_cursos)

def tipos_avaliacoes(request):
    tipos_avaliacoes = {
        'tipos_avaliacoes': Tipos_Avaliacoes.objects.all()
    }

    return render(request, 'tipos_avaliacoes/tipos_avaliacoes.html', tipos_avaliacoes)







  


