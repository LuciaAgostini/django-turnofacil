from django.urls import path

from .views import (
    lista_turnos,
    lista_profesionales,
    crear_turno,
    editar_turno,
    eliminar_turno
)

urlpatterns = [

    path(
        '',
        lista_turnos,
        name='lista_turnos'
    ),

    path(
        'profesionales/',
        lista_profesionales,
        name='lista_profesionales'
    ),

    path(
        'crear/',
        crear_turno,
        name='crear_turno'
    ),

    path(
        'editar/<int:id>/',
        editar_turno,
        name='editar_turno'
    ),

    path(
        'eliminar/<int:id>/',
        eliminar_turno,
        name='eliminar_turno'
    ),
]