from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_page(request):
    category = request.GET.get("cat")
    sort = request.GET.get("sort")

    data = {
        'title': 'Space Of Taste'
        }

    if category != None:
        category = "All"

    return render(request, 'main/index.html', data)