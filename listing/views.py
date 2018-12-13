from .models import Category, Listing
from django.shortcuts import render, get_object_or_404


def index(request):
    all_categories = Category.objects.all()
    return render(request, 'listing/index.html',  { 'all_categories': all_categories })

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'listing/detail.html', {"category":category})

def favorite(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    try:
        selected_good = category.good_set.get(pk=request.POST['listing'])
    except (KeyError, Listing.DoesNotExist):
        return render(request, 'listing/detail.html', {"category":category, "error_message": "You did not select a valid listing"} )
    else:
        selected_good.is_favorite = True
        selected_good.save()
        return render(request, 'listing/detail.html', {"category":category})
