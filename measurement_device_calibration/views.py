from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *

class MeasurementDeviceCreateView(CreateView):
    success_url = '/measure/'
    model = MeasurementDevice
    fields = '__all__'
class MeasurementDeviceUpdateView(UpdateView):
    success_url = '/measure/'
    model = MeasurementDevice
    fields = '__all__'
class MeasurementDeviceDeleteView(DeleteView):
    success_url = '/measure/'
    model = MeasurementDevice
    fields = '__all__'
class MeasurementDeviceListView(ListView):
    model = MeasurementDevice
    fields = '__all__'