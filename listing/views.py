from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category, Listing


class IndexView(generic.ListView):
    template_name = 'listing/index.html'
    context_object_name = 'all_categories'
    def get_queryset(self):
        return Category.objects.all()

class DetailView(generic.DetailView):
    model = Category
    template_name = 'listing/detail.html'


class CategoryCreate(CreateView):
    model = Category
    fields = ['name', 'description', 'category_logo']

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['name', 'description', 'category_logo']

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('listing:index')
