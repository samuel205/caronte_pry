# API Django-rest

Aplicación para la visualización de datos de la API de pokemon 

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/samuel205/caronte_pry.git
   cd tu-proyecto
   
2. Instala las dependencias
   ```bash
   pip install -r req.txt
3. Ejecuta migraciones
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
## Migración de datos
Para cargar datos iniciales en la base de datos, ejecuta el siguiente script:
```bash
python runback/migrar_pokemonapi.py
```

## Ejecutar el Proyecto

Una vez que las migraciones se hayan ejecutado y los datos iniciales se hayan cargado, puedes ejecutar el proyecto con:
```bash
python manage.py runserver
```
Visita http://localhost:8000/ en tu navegador para ver el sitio en desarrollo.

El proyecto está desplegado en https://sveram.pythonanywhere.com/. Puedes visitar el sitio en línea para ver la versión en producción.


