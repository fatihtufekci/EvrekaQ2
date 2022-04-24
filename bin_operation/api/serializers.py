from django.db.models import fields
from rest_framework import serializers
from bin_operation.models import Bin, Operation, BinOperation

class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('longitude', 'latitude')

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('name',)

class BinOperationSerializer(serializers.ModelSerializer):
    bin = BinSerializer(read_only=True)
    operation = OperationSerializer(read_only=True)
    last_collection = serializers.SerializerMethodField()
    
    class Meta:
        model = BinOperation
        fields = ('bin', 'operation', 'collection_frequency', 'last_collection')

    def get_last_collection(self, obj):
        return f'{obj.last_collection.strftime("%Y-%m-%d %H:%M:%S")}'