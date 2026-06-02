from django.contrib import admin

from .models import Turno, Profesional


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):

    list_display = (
        'cliente',
        'fecha',
        'hora',
        'profesional'
    )

    search_fields = (
        'cliente',
    )

    list_filter = (
        'fecha',
        'profesional'
    )


@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'especialidad'
    )

    search_fields = (
        'nombre',
    )