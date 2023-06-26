
from django.contrib import admin
from django.urls import path, include
from usuario.router import router as usuario_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(usuario_router.urls)),
]
