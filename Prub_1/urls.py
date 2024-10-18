
from django.contrib import admin
from django.urls import path
from Formu_1 import views
from Formu_1.views import MiVista


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/datos/', MiVista.as_view(), name='mi-vista'),
    path('uploaded-info/', views.get_uploaded_info, name='get_uploaded_info'),
]
