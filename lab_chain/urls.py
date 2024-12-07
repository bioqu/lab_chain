from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuario import views as usuario_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("consola.urls")),
    path("registro/", usuario_views.registro, name="usuario-registro"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   