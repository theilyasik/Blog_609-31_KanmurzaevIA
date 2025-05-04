from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {"header": "Homepage", "message": "Welcome to My Site!"}
    return render(request, 'homepage.html', context=data)

def about(request):
    header = "About us"
    staff = ['sb', 'sb', 'sb']
    director = {"name": "Ilyas", "img": '/director.jpg'}
    address = ('Somewhere in' ' Surgut', "" 'Russia')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)