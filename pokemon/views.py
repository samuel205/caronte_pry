import requests
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from rest_framework import generics
from pokemon.models import Pokemon
from pokemon.serializers import PokemonSerializer


# Create your views here.
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 20  # Número de elementos por página
    page_query_param = 'page'  # Parámetro para especificar el número de página en la URL
    page_size_query_param = 'limit'  # Parámetro para especificar el tamaño de la página en la URL

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'prev': self.get_previous_link(),
            'results': data
        })


class PokemonAPIView(generics.ListAPIView):
    serializer_class = PokemonSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        search = self.request.query_params.get('search', None)
        if search:
            return Pokemon.objects.filter(name__icontains=search)
        return Pokemon.objects.all()