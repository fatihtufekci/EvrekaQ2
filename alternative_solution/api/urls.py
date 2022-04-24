from django.urls import path
from alternative_solution.api import views as api_views


urlpatterns = [
    path('bin-garbage-collection-operations/', api_views.GarbageCollectionOperationViewSet.as_view({'get': 'list'})),
    path('bin-paper-collection-operations/', api_views.PaperCollectionOperationViewSet.as_view({'get': 'list'})),
]