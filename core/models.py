from django.db import models

from django.db import models

class ReservaPabellon(models.Model):
    # Información del médico
    nombre_medico = models.CharField(max_length=100)  # Nombre del médico
    rut_medico = models.CharField(max_length=20)  # RUT del médico
    especialidad = models.CharField(max_length=100)  # Especialidad del médico

    # Información de la cirugía
    tipo_cirugia = models.CharField(max_length=100)  # Tipo de cirugía

    # Información del paciente
    nombre_paciente = models.CharField(max_length=100)  # Nombre del paciente
    rut_paciente = models.CharField(max_length=20)  # RUT del paciente

    # Detalles de la reserva
    fecha = models.DateField()  # Fecha de la reserva
    hora = models.TimeField()  # Hora de la reserva
    equipo_medico = models.CharField(max_length=200)  # Equipo médico necesario

    # Representación en el admin y otros contextos
    def __str__(self):
        return f"{self.nombre_paciente} - {self.tipo_cirugia} - {self.fecha} {self.hora}"
