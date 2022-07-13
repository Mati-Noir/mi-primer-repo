from django.contrib import admin
from django.urls import path
from mi_app.views import (saludar_a, saludo, 
        saludo_personalizado, listar_cursos, listar_estudiantes,
         mostrar_index, formulario_curso, formulario_busqueda,
        actualizar_curso, confirmar_borrar_curso,borrar_curso)


urlpatterns = [
    path('mi-pagina/', mostrar_index),
    path('saludar/persona/<nombre>', saludar_a),
    path('saludo-personalizado/', saludo_personalizado),
    path('listar-cursos/', listar_cursos),
    path('listar-estudiantes/', listar_estudiantes),
    path('formulario/', formulario_curso),
    path('buscar/', formulario_busqueda),
    path('curso/<pk>/actualizar', actualizar_curso, name="curso-actualizar"),
    path('curso/<pk>/confirmar-borrar', confirmar_borrar_curso, name="curso-confirmar-borrar"),
    path('curso/<pk>/borrar', borrar_curso, name="curso-borrar"),
]