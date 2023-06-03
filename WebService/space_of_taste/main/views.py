from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_page(request):
    category = request.GET.get("cat")
    sort = request.GET.get("sort")

    if category != None:
        category = "All"

    return HttpResponse(f'<h1>Sort: {sort}, Category: {category}</h1>')