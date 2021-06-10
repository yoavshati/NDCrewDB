from django.urls import path

from .views import *

urlpatterns = [
    path('', MeasurementDeviceListView.as_view(), name='item-list'),
    path('new/', MeasurementDeviceCreateView.as_view(), name='item-create'),
    path('update/<int:pk>/', MeasurementDeviceUpdateView.as_view(), name='item-update'),
    path('delete/<int:pk>/', MeasurementDeviceDeleteView.as_view(), name='item-delete'),
    ]