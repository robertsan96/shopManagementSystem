from django.shortcuts import render
from .models import Category, Item
# Create your views here.


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    categories = Category.objects.all()
    items = Item.objects.all()
    context = {'categories': categories,
               'items': items}
    return render(request, 'app/index.html', context)

def category_items(request, category):
    categories = Category.objects.all()
    items = Item.objects.filter(category__name=category)
    context = {'categories': categories,
               'items': items}
    return render(request, 'app/index.html', context)

def item_details(request, item_id):
    categories = Category.objects.all()
    try:
        item = Item.objects.get(pk=item_id)
    except:
        items = Item.objects.all()
        context = {
            'categories': categories,
            'items': items}
        return render(request, 'app/index.html', context)

    context = {'categories': categories,
               'item': item}
    return render(request, 'app/details.html', context)
