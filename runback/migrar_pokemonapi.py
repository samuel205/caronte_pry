#!/usr/bin/env python
import os
import sys

import django
import requests
from django.db import transaction
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caronte.settings')
application = get_wsgi_application()
# Configura Django
django.setup()

from pokemon.models import Pokemon

pagination_offset = 0
max_paging = 1280
count = 1
with transaction.atomic():
    try:
        for p in range(pagination_offset,max_paging,20):
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset={p}&limit=20')
            pokemon_data = response.json()['results']
            for pokemon in pokemon_data:
                if not Pokemon.objects.filter(name=pokemon['name']).exists():
                    pkm = Pokemon.objects.create(name=pokemon['name'])
                    print(f"{count}.- Pokemon {pkm.name} creado")
                    count +=1
                else:
                    print(f"El pokemon {pokemon['name']} ya existe en la base")
        print(f"Se han creado {count} pokemons")
    except Exception as ex:
        transaction.set_rollback(True)
        print(f"Error: {ex} ({sys.exc_info()[-1].tb_lineno})")
    finally:
        print("****************************El proceso ha finalizado*********************************")

