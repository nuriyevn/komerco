from django.http import Http404
from .models import Category
from django.shortcuts import render

def index(request):
    all_categories = Category.objects.all()
    return render(request, 'good/index.html',  { 'all_categories': all_categories })

def detail(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category does not exist")
    return render(request, 'good/detail.html', {"category":category})

