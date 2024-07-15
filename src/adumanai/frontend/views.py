from django.http import HttpResponse
from django.shortcuts import render
from .models import cakes_collections
from .models import Cakes
from .forms import FormCake
import datetime



# def index(request):
#     cakes = cakes_collections.find()
#     return HttpResponse(cakes)

def index(request):
    my_dict = {"insert_me": "Hello this is from view.py!"}
    return render(request,'frontend/index.html',context=my_dict)

def push_data_view(request):
    form = FormCake()
    if request.method == 'POST':
        form = FormCake(request.POST)
        
        if form.is_valid():
            print("Validations Good")
            cake = Cakes()
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            url = form.cleaned_data['url']
            cake.update(name,description,url)
    return render(request, 'frontend/form_page.html', {'form': form}) 

