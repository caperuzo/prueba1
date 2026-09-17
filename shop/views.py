from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, 'shop/inicio.html', {
        'productos': productos,
        'total_productos': len(productos),
    })


def detalle(request, id):
    producto = next((p for p in productos if p['id'] == id), None)
    return render(request, 'shop/detalle.html', {'producto': producto})
  
productos = [
    {
        'id': 1, 'nombre': 'Horizon Forbidden West', 'plataforma': 'PS5',
        'genero': 'Aventura', 'anio': 2022, 'desarrollador': 'Guerrilla Games',
        'precio': 39.99, 'descripcion': 'Explora un mundo abierto lleno de misterios.',
    },
    {
        'id': 2, 'nombre': 'The Legend of Zelda: Tears of the Kingdom', 'plataforma': 'Switch',
        'genero': 'Aventura', 'anio': 2023, 'desarrollador': 'Nintendo',
        'precio': 59.99, 'descripcion': 'Descubre nuevos cielos y secretos de Hyrule.',
    },
    {
        'id': 3, 'nombre': 'Elden Ring', 'plataforma': 'PC', 'genero': 'RPG',
        'anio': 2022, 'desarrollador': 'FromSoftware',
        'precio': 49.99, 'descripcion': 'Enfrenta desafíos en las Tierras Intermedias.',
    },
    {
        'id': 4, 'nombre': 'Forza Horizon 5', 'plataforma': 'Xbox Series',
        'genero': 'Carreras', 'anio': 2021, 'desarrollador': 'Playground Games',
        'precio': 34.99, 'descripcion': 'Corre por los paisajes de México.',
    },
    {
        'id': 5, 'nombre': 'Baldur’s Gate 3', 'plataforma': 'PC',
        'genero': 'RPG', 'anio': 2023, 'desarrollador': 'Larian Studios',
        'precio': 54.99, 'descripcion': 'Crea tu grupo y decide el destino de los Reinos.',
    },
    {
        'id': 6, 'nombre': 'Super Mario Bros. Wonder', 'plataforma': 'Switch',
        'genero': 'Plataformas', 'anio': 2023, 'desarrollador': 'Nintendo',
        'precio': 44.99, 'descripcion': 'Disfruta una aventura clásica llena de sorpresas.',
    },
]