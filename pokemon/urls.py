from django.urls import re_path, include

from pokemon.views import PokemonAPIView

urlpatterns = [
    re_path(r"^caronte/", PokemonAPIView.as_view(), name='api_view_pokemon')
]