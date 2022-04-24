from django.contrib import admin
from .models import Bin, GarbageCollectionOperation, PaperCollectionOperation

admin.site.register(Bin)
admin.site.register(GarbageCollectionOperation)
admin.site.register(PaperCollectionOperation)
