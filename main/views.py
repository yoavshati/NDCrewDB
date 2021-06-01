from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from .models import *
from .forms import *

def home(request):
    return render(request, 'main/home.html')

class TestList(ListView):
    model = Test

class TestDetail(DetailView):
    model = Test

def add_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TestForm()
    
    if 'submit' in request.POST:
        return HttpResponseRedirect('/')
    elif 'add_more' in request.POST:
        pass # clear changing fields

    return render(request, 'main/add_test.html', {"form": form})

def get_items(request):
    item_list = list(ReferanceItem.objects.values_list('part_description', flat=True).order_by('part_description'))
    return JsonResponse({'item_list': item_list})

def get_item(request, name):
    item = model_to_dict(ReferanceItem.objects.get(part_description__iexact=name))
    return JsonResponse(item)

class TestUpdate(UpdateView):
    model = Test
    fields = '__all__'

class TestDelete(DeleteView):
    model = Test