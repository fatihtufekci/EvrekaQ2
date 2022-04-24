from django.db.models import fields
from rest_framework import serializers
from alternative_solution.models import GarbageCollectionOperation, PaperCollectionOperation


class GarbageCollectionOperationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GarbageCollectionOperation
        fields = ('bin', 'name', 'collection_frequency')


class PaperCollectionOperationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaperCollectionOperation
        fields = ('bin', 'name', 'collection_frequency')