from django.shortcuts import render
from rest_framework import generics, mixins

from .serializers import CategoriesSerializer
from .models import Categories

# Create your views here.
class CategoriesView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = CategoriesSerializer

    def get_queryset(self):
        return Categories.objects.all()

    def post(self, request, *args, **kwargs):
        self.create(request, args, kwargs)

class CategoriesRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoriesSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Categories.objects.all()
