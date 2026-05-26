from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Turno

from .forms import TurnoForm


def lista_turnos(request):

    turnos = Turno.objects.all()

    return render(
        request,
        'lista_turnos.html',
        {
            'turnos': turnos
        }
    )


def crear_turno(request):

    if request.method == 'POST':

        form = TurnoForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('lista_turnos')

    else:

        form = TurnoForm()

    return render(
        request,
        'form_turno.html',
        {
            'form': form
        }
    )


def editar_turno(request, id):

    turno = get_object_or_404(
        Turno,
        id=id
    )

    if request.method == 'POST':

        form = TurnoForm(
            request.POST,
            instance=turno
        )

        if form.is_valid():

            form.save()

            return redirect('lista_turnos')

    else:

        form = TurnoForm(instance=turno)

    return render(
        request,
        'form_turno.html',
        {
            'form': form
        }
    )


def eliminar_turno(request, id):

    turno = get_object_or_404(
        Turno,
        id=id
    )

    if request.method == 'POST':

        turno.delete()

        return redirect('lista_turnos')

    return render(
        request,
        'eliminar_turno.html',
        {
            'turno': turno
        }
    )