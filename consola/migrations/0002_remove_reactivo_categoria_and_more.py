# Generated by Django 5.1.dev20240419123637 on 2024-10-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consola", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reactivo",
            name="categoria",
        ),
        migrations.AddField(
            model_name="reactivo",
            name="condiciones_almacenamiento",
            field=models.CharField(
                choices=[
                    ("ambiente", "Temperatura ambiente"),
                    ("refrigerador_4", "Refrigerador (4°C)"),
                    ("congelador_20", "Congelador (-20°C)"),
                    ("congelador_80", "Congelador (-80°C)"),
                ],
                default="ambiente",
                max_length=20,
                verbose_name="Condiciones de Almacenamiento",
            ),
        ),
        migrations.AddField(
            model_name="reactivo",
            name="fecha_adquisicion",
            field=models.DateField(
                blank=True, null=True, verbose_name="Fecha de Adquisición"
            ),
        ),
        migrations.AlterField(
            model_name="reactivo",
            name="unidad",
            field=models.CharField(
                choices=[
                    ("g", "Gramos"),
                    ("mg", "Miligramos"),
                    ("UL", "microlitros"),
                    ("mL", "Mililitros"),
                    ("L", "Litros"),
                ],
                default="g",
                max_length=100,
            ),
        ),
    ]