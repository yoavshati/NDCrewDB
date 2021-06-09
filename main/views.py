from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from .models import *
from .forms import TestForm, ItemFormSet

#############
#   views   #
#############

def home(request):
    return render(request, 'main/home.html')

class TestListView(ListView):
    model = Test

# creates test and related parts
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

# REFERENCE ITEM
class ItemCreateView(CreateView):
    model = ReferenceItem
    fields = '__all__'
class ItemUpdateView(UpdateView):
    model = ReferenceItem
    fields = '__all__'
class ItemDeleteView(DeleteView):
    model = ReferenceItem
    fields = '__all__'
class ItemListView(ListView):
    model = ReferenceItem
    fields = '__all__'

###########
#   API   #
###########

def get_items(request):
    item_list = list(ReferanceItem.objects.values_list('part_description', flat=True).order_by('part_description'))
    return JsonResponse({'item_list': item_list})

def get_item(request, name):
    item = model_to_dict(ReferanceItem.objects.get(part_description__iexact=name))
    return JsonResponse(item)