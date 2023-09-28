"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index.html'),
    path('pessoas/', pessoas, name='pessoas' ),
    path('cidades/', cidades, name='cidades' ),
    path('ocupacoes/', ocupacoes, name='ocupacoes'),
    path('instituicoes/', instituicoes, name='instituicoes' ),
    path('areas_do_saber/', areas_do_saber, name='areas_do_saber' ),
    path('cursos/', cursos, name='Cursos' ),
    path('periodos/', periodos, name='Periodos' ),
    path('disciplinas/', disciplinas, name='Diciplinas' ),
    path('matriculas/', matriculas, name='Matriculas' ),
    path('avaliacoes/', avaliacoes, name='Avaliacoes' ),
    path('frequencias/', frequencias, name='Frequencias' ),
    path('turmas/', turmas, name='Turmas' ),
    path('ocorrencias/', ocorrencias, name='Ocorrencias' ),
    path('disciplinas_cursos/', disciplinas_cursos, name='Disciplinas_Cursos' ),
    path('tipos_avaliacoes/', tipos_avaliacoes, name='Tipos_Avaliacoes' ),












]