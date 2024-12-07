from django.contrib import admin
from .models import Reactivo, Experimento, ReactivoUsado
from django.contrib.auth.models import Group

# Titulo de sitio admin 
admin.site.site_header = 'Consola administracion LabChain'

# Creacion de clase para admin de reactivos
class reactivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_total', 'cantidad_por_unidad', 'unidad', 'empresa')
    # TODO: Se puede cambiar como se muestra cantidad total, pero todavia no se que nombre deberia llevar
    """ def mostrar_cantidad_total(self, obj):
        return f"{obj.cantidad_total} {obj.unidad}"
    mostrar_cantidad_total.short_description = 'Items' """
    list_filter = ('nombre', 'empresa', 'cantidad_total')

# Admin site reactivo
admin.site.register(Reactivo, reactivoAdmin)

# Admin site experimento
class ReactivoUsadoInline(admin.TabularInline):
    model = ReactivoUsado
    extra = 1  # Número de filas adicionales en blanco

class ExperimentoAdmin(admin.ModelAdmin):
    inlines = [ReactivoUsadoInline]
    list_display = ('nombre', 'staff', 'fecha', 'reactivos_usados')

    def reactivos_usados(self, obj):
        # Obtén los reactivos usados desde el modelo intermedio
        reactivos = obj.reactivos.through.objects.filter(experimento=obj)
        # Crea una lista con los detalles de cada reactivo
        detalles = [
            f"{reactivo.reactivo.nombre}: {reactivo.cantidad_usada} {reactivo.reactivo.unidad}" 
            for reactivo in reactivos
        ]
        return ", ".join(detalles)

    reactivos_usados.short_description = 'Reactivos Usados'

admin.site.register(Experimento, ExperimentoAdmin)
