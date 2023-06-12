from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def main_page(request):

    data = {
        'title': 'Space Of Taste',
        'category':[],
        'dish':[],
    }

    cat= request.GET.get("cat")
    sort = request.GET.get("sort")

    if cat != None:
        dish=Dish.objects.filter(category = cat)
    else:
        dish = Dish.objects.all()

    vse=Category.objects.all()

    for i in dish:
        data['dish'].append({'name': i.name, 'img': i.image, 'cat': i.categori, 'des': i.description, 'opt': i.options})
    
    for i in vse:
        data['category'].append({'name': i.name, 'icon': i.icons})

    return render(request, 'main/index.html', data)