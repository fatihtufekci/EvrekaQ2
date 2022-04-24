from django.urls import path
from bin_operation.api import views as api_views


urlpatterns = [
    path('bin-operations/', api_views.BinOperationViewSet.as_view({'get': 'list'})),
]