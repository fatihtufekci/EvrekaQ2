from django.db import models


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return f'{self.latitude} - {self.longitude}'

class Operation(models.Model):
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class GarbageCollectionOperation(Operation):
    name = models.CharField(max_length=120)


class PaperCollectionOperation(Operation):
    name = models.CharField(max_length=120)
