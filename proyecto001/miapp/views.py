from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Docente
# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>
            <a href="/index">Saludo</a>
        </li>
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

def integrantes(request):
    return render(request, "integrantes.html")

def index(request):
    return render(request, "index.html")

def saludo(request):
    return render(request,'saludo.html')

def listar_docentes(request):
    docentes = Docente.objects.all()  # Obtener todos los docentes desde la base de datos
    return render(request, 'listar_docentes.html', {'docentes': docentes})

def eliminar_docente(request, id_docente):
    docente = get_object_or_404(Docente, id=id_docente)
    docente.delete()
    return HttpResponseRedirect(reverse('listar_docentes'))

def agregar_docente(request):
    if request.method == 'POST':
        # Procesar el formulario cuando se envía
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        dni = request.POST.get('dni')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        estado = request.POST.get('estado') == 'activo'

        # Crear un nuevo docente
        nuevo_docente = Docente(
            codigo=codigo,
            nombre=nombre,
            apellido_paterno=apellido_paterno,
            apellido_materno=apellido_materno,
            dni=dni,
            fecha_nacimiento=fecha_nacimiento,
            estado=estado
        )
        nuevo_docente.save()

        # Redirigir a la página de listar_docentes
        return redirect('listar_docentes')
    else:
        # Manejar la solicitud GET
        return render(request, 'agregar_docente.html')

def listar_cursos(request):
    return render(request, 'listar_cursos.html')

def agregar_curso(request):
    return render(request, 'agregar_curso.html')