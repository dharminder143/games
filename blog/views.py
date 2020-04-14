from django.shortcuts import render
from .models import *
from django.shortcuts import render , redirect , get_object_or_404
# Create your views here.
from .resources import PersonResource
from tablib import Dataset
from django.db.models import Q
from django.contrib import messages


def product(request):
	post = Product.objects.all() 
	action = Product.objects.filter(category='Action')
	return render(request,'blog/index.html',{'posts':post,
												'actions':action,
												}) 

def post(request):
	post = Product.objects.all() 
	action = Product.objects.filter(category='Action')
	return render(request,'blog/single-game.html',{'posts':post,
												'actions':action,
												})  
def post_action(request):
	action = Product.objects.filter(category='Action')
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
    return render(request,'blog/search.html',{'allpost':allpost, 'query':query})