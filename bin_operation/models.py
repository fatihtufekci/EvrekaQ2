from django.db import models


class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.latitude} - {self.longitude}'

class Operation(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.name}'


class BinOperation(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE, related_name="operation_bins")
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, related_name="bin_operations")
    collection_frequency = models.IntegerField(default=0)
    last_collection = models.DateTimeField()

    def __str__(self):
        return f'{self.operation.name} - ({self.bin.longitude},{self.bin.latitude}) - {self.collection_frequency} - {self.last_collection.strftime("%Y-%m-%d %H:%M:%S")}'
