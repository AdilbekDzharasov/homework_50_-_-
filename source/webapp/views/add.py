from webapp.db import Cat
from django.shortcuts import redirect


def add_cat(request):
    name = request.POST.get('name')
    Cat.add(name)
    return redirect('http://localhost:8000/cat_stats/')
