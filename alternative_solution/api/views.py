from rest_framework import viewsets

from alternative_solution.api.serializers import GarbageCollectionOperationSerializer, PaperCollectionOperationSerializer
from alternative_solution.models import GarbageCollectionOperation, PaperCollectionOperation


class GarbageCollectionOperationViewSet(viewsets.ModelViewSet):
    queryset = GarbageCollectionOperation.objects.select_related().all()
    serializer_class = GarbageCollectionOperationSerializer


class PaperCollectionOperationViewSet(viewsets.ModelViewSet):
    queryset = PaperCollectionOperation.objects.select_related().all()
    serializer_class = PaperCollectionOperationSerializer