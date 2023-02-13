from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Включая URL-адреса из приложения flatpages.
    path('pages/', include('django.contrib.flatpages.urls'))
]
