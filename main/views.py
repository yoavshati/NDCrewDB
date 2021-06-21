from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms.models import model_to_dict
from .models import *
from .forms import TestForm, ItemFormSet, UserForm, PasswordForm
from .filters import *

#############
#   views   #
#############

def home(request):
    return render(request, 'main/home.html')

class TestListView(ListView):
    model = Test

def test_list(request):
    items = TestItem.objects.all()
    item_filter = ItemFilter(request.GET, queryset = items)
    test_list = Test.objects.filter(id__in=item_filter.qs.values_list('test', flat = True)).distinct()
    test_filter = TestFilter(request.GET, queryset = test_list)
    test_list = test_filter.qs
    return render(request, 'main/test_list.html', {
        'object_list': test_list,
        'test_filter': test_filter,
        'item_filter': item_filter
    })

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
    success_url = '/item/'
    model = ReferenceItem
    fields = '__all__'
class ItemUpdateView(UpdateView):
    success_url = '/item/'
    model = ReferenceItem
    fields = '__all__'
class ItemDeleteView(DeleteView):
    success_url = '/item/'
    model = ReferenceItem
class ItemListView(ListView):
    model = ReferenceItem

# USER
def technician_list(request):
    technicians = User.objects.filter(groups__name = 'טכנאי')
    # filter again so supervisors can only see their own technicians
    if request.user.groups.name == 'מ"ע':
        technicians = technicians.filter(department = request.user.department)
    return render(request, 'main/user_list.html', {'object_list': technicians})

def user_detail(request, id):
    technician = User.objects.get(id=id)
    tests = technician.tested.all()
    context = {'technician': technician}
    methods = [
        'PT',
        'MT',
        'EC',
        'UT',
        'RT',
        'visual',
        'tap',
        'PAUT',
        'LST',
        'IRT'
    ]
    for i in range(10):
        hours = 0
        for test in tests:
            hours += sum(test.items.filter(test_method = i+1).values_list('testing_hours', flat = True))
        context[methods[i]] = hours
    return render(request, 'main/user_profile.html', context)

def user_register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        if 'save' in request.POST:
            return HttpResponseRedirect('/technician')
        elif 'add_more' in request.POST:
            return HttpResponseRedirect('/technician/new')
    return render(request, 'main/user_form.html', {'form': form})
    
class UserUpdateView(UpdateView):
    success_url = '/technician/'
    model = User
    fields = '__all__'
    exclude = ['password']
    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

@login_required
def change_password(request, id):
    form = PasswordForm(request.POST or None)
    user = User.objects.get(id=id)
    if form.is_valid():
        user.set_password(form.cleaned_data['new_password'])
        user.save()
        return HttpResponseRedirect('/')
    return render(request, 'main/change_password.html', {'form': form, 'technician': user})

###########
#   API   #
###########

def get_items(request):
    item_list = list(ReferenceItem.objects.values_list('part_description', flat=True).order_by('part_description'))
    return JsonResponse({'item_list': item_list})

def get_item(request, name):
    item = model_to_dict(ReferenceItem.objects.get(part_description__iexact=name))
    return JsonResponse(item)