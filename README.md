# GameVault

Catálogo de videojuegos desarrollado con Python 3.13 y Django 5.2.

## Ejecución

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego visita http://127.0.0.1:8000/.

Los datos se encuentran en `shop/views.py` como una lista de diccionarios.
No se usan modelos propios ni una base de datos para el catálogo.

Se utilizó IA como apoyo para revisar la estructura HTML, la navegación y los requisitos de la pauta; posteriormente se adaptó el código al proyecto.
