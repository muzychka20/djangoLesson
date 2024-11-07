from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Main Page!!',
        'values': ['hello', 'some', 'text', 'here'],
        'obj': {
            'car': 'Audi',
            'age': 18,
            'hobby': 'Football',
        },
    }
    return render(request, 'main/index.html', data) # HttpResponse("<h4>Hello</h4>")

def about(request):
    return render(request, 'main/about.html') # HttpResponse("<h4>about</h4>")