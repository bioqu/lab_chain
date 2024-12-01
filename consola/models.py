from django.db import models

class reactivo(models.Model):
    nombre = models.CharField(max_length=150)
    cantidad = models.DecimalField(max_digits=10, decimal_places=3)
    unidad = models.CharField(
        max_length=100,
        choices=[('g', 'Gramos'), ('mg', 'Miligramos'),('UL', 'microlitros'), ('mL', 'Mililitros'), ('L', 'Litros'), ],
        default='g'  # Puedes poner la unidad que más te convenga como default
    )

    # Campo para la fecha de adquisición
    fecha_adquisicion = models.DateField(null=True, blank=True, verbose_name="Fecha de Adquisición")

    # Campo para las condiciones de almacenamiento
    OPCIONES_TEMPERATURA = [
        ('ambiente', 'Temperatura ambiente'),
        ('refrigerador_4', 'Refrigerador (4°C)'),
        ('congelador_20', 'Congelador (-20°C)'),
        ('congelador_80', 'Congelador (-80°C)'),
    ]
    condiciones_almacenamiento = models.CharField(
        max_length=20,
        choices=OPCIONES_TEMPERATURA,
        default='ambiente',
        verbose_name="Condiciones de Almacenamiento"
    )


    def __str__(self):
        return f'{self.nombre} ({self.cantidad} {self.unidad})'
