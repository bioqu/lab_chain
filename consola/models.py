from django.db import models

# Create your models here.
class reactivo(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=3)
    unidad = models.CharField(
        max_length=10,
        choices=[('g', 'Gramos'), ('mg', 'Miligramos'), ('ml', 'Mililitros')],
        default='g'  # Puedes poner la unidad que más te convenga como default
    )

    def __str__(self):
        return f'{self.nombre} ({self.cantidad} {self.unidad})'
