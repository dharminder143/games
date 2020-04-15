from django.shortcuts import render
from .models import *
from django.shortcuts import render , redirect , get_object_or_404
# Create your views here.
from .resources import PersonResource
from tablib import Dataset
from django.db.models import Q , Count
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def product(request):
    postss=Product.objects.values('category').distinct()
    post = Product.objects.filter(category__in=[item['category'] for item in postss])[:7]
    action = Product.objects.filter(category='Action')[:10]
    return render(request,'blog/index.html',{'posts':post,
												'actions':action,
												}) 

def post(request):
    post = Product.objects.all()
    paginator = Paginator(post, 12)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request,'blog/single-game.html',{'posts':post,											
												})  
def post_action(request):
    action = Product.objects.filter(category='Action')
    paginator = Paginator(action, 12)
    page = request.GET.get('page')
    action = paginator.get_page(page)
    return render(request,'blog/action-game.html',{'actions':action,
												})  


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'blog/import.html')

def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allpost= Product.objects.none()
    else:
        allpost=Product.objects.filter(Q(category__icontains=query)|
                                        Q(gamename__icontains=query)|
                                        Q(vendor__icontains=query))
    if allpost.count() == 0:
        messages.error(request,'can not found')
    paginator = Paginator(allpost, 12)
    page = request.GET.get('page')
    try:
        allpost = paginator.page(page)
    except PageNotAnInteger:
        allpost = paginator.page(1)
    except EmptyPage:
        allpost = paginator.page(paginator.num_pages)
    # allpost = paginator.get_page(page)
    return render(request,'blog/search.html',{'allpost':allpost, 'query':query})



