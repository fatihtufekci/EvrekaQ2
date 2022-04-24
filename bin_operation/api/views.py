from rest_framework import viewsets

from bin_operation.api.serializers import BinOperationSerializer
from bin_operation.models import BinOperation


class BinOperationViewSet(viewsets.ModelViewSet):
    queryset = BinOperation.objects.all()
    serializer_class = BinOperationSerializer