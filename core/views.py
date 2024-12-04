from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import ReservaPabellon
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ReservaPabellon
from .serializers import ReservaPabellonSerializer

def agendar_pabellon(request):
    if request.method == 'POST':
        # Capturar los datos del formulario
        nombre_medico = request.POST.get('nombre_medico')
        rut_medico = request.POST.get('rut_medico')
        especialidad = request.POST.get('especialidad')
        tipo_cirugia = request.POST.get('tipo_cirugia')
        nombre_paciente = request.POST.get('nombre_paciente')
        rut_paciente = request.POST.get('rut_paciente')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        equipo_medico = request.POST.get('equipo_medico')

        # Crear una nueva reserva
        ReservaPabellon.objects.create(
            nombre_medico=nombre_medico,
            rut_medico=rut_medico,
            especialidad=especialidad,
            tipo_cirugia=tipo_cirugia,
            nombre_paciente=nombre_paciente,
            rut_paciente=rut_paciente,
            fecha=fecha,
            hora=hora,
            equipo_medico=equipo_medico,
        )

        # Redirigir a una página de confirmación (o recargar el formulario)
        return redirect('agendar_pabellon')

    return render(request, 'agendar_pabellon.html')

class ReservaPabellonList(APIView):
    def get(self, request):
        reservas = ReservaPabellon.objects.all()
        serializer = ReservaPabellonSerializer(reservas, many=True)
        return Response(serializer.data)

