# Generated by Django 5.1.dev20240419123637 on 2024-12-05 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consola", "0002_alter_reactivo_cantidad_por_unidad"),
    ]

    operations = [
        migrations.AddField(
            model_name="reactivo",
            name="empresa",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
