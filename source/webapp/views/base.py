from django.shortcuts import render


def index_cat(request):
    return render(request, 'index.html')

