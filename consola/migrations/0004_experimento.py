# Generated by Django 5.1.dev20240419123637 on 2024-12-07 21:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consola", "0003_reactivo_empresa"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Experimento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=150)),
                ("cantidad_usada", models.FloatField(null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "Reactivo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="consola.reactivo",
                        verbose_name="Reactivo para experimentos",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuario",
                    ),
                ),
            ],
        ),
    ]
