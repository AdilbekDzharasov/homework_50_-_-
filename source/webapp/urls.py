from django.urls import path

from webapp.views.base import index_cat
from webapp.views.add import add_cat
from webapp.views.game import game_cat

urlpatterns = [
    path('', index_cat),
    path('add/', add_cat),
    path('cat_stats/', game_cat),
]

