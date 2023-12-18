from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/index">Saludo</a>
        </li>
        <li>
            <a href="/listar_docentes">Docentes</a>
        </li>
        <li>
            <a href="/agregar_docente">Crear Docente</a>
        </li>
        <li>
            <a href="/listar_cursos">Cursos</a>
        </li>
        <li>
            <a href="/agregar_curso">Crear Curso</a>
        </li>
        <li>
            <a href="/integrantes">Integrantes</a>
        </li>
    </ul>
    <hr/>
"""

def listar_docentes(request):
    return render(request, "listar_docentes.html")

def agregar_docente(request):
    return render(request, 'agregar_docente.html')

def listar_cursos(request):
    return render(request, 'listar_cursos.html')

def agregar_curso(request):
    return render(request, 'agregar_curso.html')

def index(request):
    return render(request, "index.html")

def saludo(request):
    return render(request,'saludo.html')

def integrantes(request):
    return render(request, "integrantes.html")