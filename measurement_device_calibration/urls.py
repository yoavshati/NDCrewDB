from django.urls import path

from .views import *

urlpatterns = [
    path('', MeasurementDeviceListView.as_view(), name='md-list'),
    path('new/', MeasurementDeviceCreateView.as_view(), name='md-create'),
    path('update/<int:pk>/', MeasurementDeviceUpdateView.as_view(), name='md-update'),
    path('delete/<int:pk>/', MeasurementDeviceDeleteView.as_view(), name='md-delete'),
    ]