from pip._vendor import requests


def user_admin(id):
    params = {'id': id}
    r = requests.get('http://localhost:3000/consultaUsuariosPorPerfil/2', params=params)
    admins = r.json()
    lista = {'admins': admins}


def get_books(year, author):
    url = 'http://api.example.com/books'
    params = {'year': year, 'author': author}
    r = requests.get('http://api.example.com/books', params=params)
    books = r.json()
    books_list = {'books':books['results']}
