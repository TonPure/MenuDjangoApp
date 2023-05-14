from django.urls import re_path, include
import menu.views as menu

urlpatterns = [
    re_path(r'^', menu.index, name='index'),
    re_path(r'^(\d+)', menu.index, name='index')
]
