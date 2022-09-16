from webapp.db import Cat
from django.shortcuts import render


def game_cat(request):
    if request.method == 'POST':
        action = request.POST.get('select-cat')
        Cat.menu(action)
    cat = Cat.cat_dict
    context = {
        'name': cat.get('name'),
        'age': cat.get('age'),
        'happiness': cat.get('happiness'),
        'satiety': cat.get('satiety'),
        'state': cat.get('state')
        }
    return render(request, 'cat.html', context=context)

