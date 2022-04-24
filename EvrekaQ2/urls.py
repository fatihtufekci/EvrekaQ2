from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('bin_operation.api.urls')),
    path('alternative-api/', include('alternative_solution.api.urls')),
]
