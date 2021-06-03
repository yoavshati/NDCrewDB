from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from .models import *
from .forms import TestForm, ItemFormSet

def home(request):
    return render(request, 'main/home.html')

class TestList(ListView):
    model = Test

class TestDetail(DetailView):
    model = Test

def add_test(request):
    test_form = TestForm()
    formset = ItemFormSet(instance=Test())
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        if test_form.is_valid():
            created_test = test_form.save(commit=False)
            formset = ItemFormSet(request.POST, instance=created_test)
            if formset.is_valid():
                created_test.save()
                formset.save()
                return HttpResponseRedirect('/')
    
    if 'submit' in request.POST:
        return HttpResponseRedirect('/')
    elif 'add_more' in request.POST:
        pass # clear changing fields

    return render(request, 'main/test_form.html', {"formset": formset, "test_form": test_form})

class TestCreateView(CreateView):
    template_name = 'main/test_form.html'
    model = Test
    form_class = TestForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = ItemFormSet()
        return self.render_to_response(self.get_context_data(form=form, item_form=item_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        item_form = ItemFormSet(self.request.POST)
        if (form.is_valid() and item_form.is_valid()):
            return self.form_valid(form, item_form)
        else:
            return self.form_invalid(form, item_form)

    def form_valid(self, form, item_form):
        """
        Called if all forms are valid. Creates a Test instance along with
        associated Items and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        item_form.instance = self.object
        item_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, item_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(form=form,item_form=item_form))

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