from django.shortcuts import render
from movie.models import Categroys


def home(request):
    context = {}
    categroys_list_all = Categroys.objects.all()
    context['categroys_list_all'] = categroys_list_all
    return render(request, 'home.html', context)
