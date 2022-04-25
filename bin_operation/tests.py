from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from bin_operation.models import Bin, Operation, BinOperation
import datetime

def populate_bin_operation_url():
    return reverse("bin-operation:bin-operations")

class BinOperationApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    @classmethod
    def setUpTestData(cls):
        cls.bin = Bin.objects.create(latitude="55.55", longitude="44.44")
        cls.operation = Operation.objects.create(name="GarbageCollectionOperation")
        cls.bin_operation = BinOperation.objects.create(
            bin=cls.bin,
            operation=cls.operation,
            collection_frequency = 3,
            last_collection = datetime.datetime(2022, 4, 25, 1, 7, 55, 744848)
        )
    
    def test_bin_operation(self):
        bin_operation = BinOperation(
            bin=self.bin,
            operation=self.operation,
            collection_frequency = 1,
            last_collection = datetime.datetime(2022, 4, 25, 1, 7, 55, 744848)
        )
        self.assertEqual(bin_operation.bin.latitude, self.bin.latitude)
        self.assertEqual(bin_operation.collection_frequency, 1)
        self.assertEqual(bin_operation.operation.name, self.operation.name)
        self.assertEqual(bin_operation.last_collection, datetime.datetime(2022, 4, 25, 1, 7, 55, 744848))
    

    def test_access_bin_operation_url(self):
        res = self.client.get("http://localhost:8000/api/bin-operations/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_bin_operation_api(self):
        res = self.client.get(populate_bin_operation_url())

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(BinOperation.objects.all().count(), 1)
    

class BinModelTest(TestCase):
    def test_vehicle(self):
        bin = Bin.objects.create(longitude="11.11", latitude="22.22")
        self.assertEqual(bin.longitude, "11.11")
        self.assertEqual(bin.latitude, "22.22")
        self.assertEqual(Bin.objects.all().count(), 1)


class OperationModelTest(TestCase):
    def test_vehicle(self):
        operation = Operation.objects.create(name="PaperCollection")
        self.assertEqual(operation.name, "PaperCollection")
        self.assertEqual(Operation.objects.all().count(), 1)