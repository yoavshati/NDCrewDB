from django.urls import path

from .views import *

urlpatterns = [
    # views
    path('', home, name='home'),
    path('test', TestList.as_view(), name='test-list'),
    path('test/new/', TestCreateView.as_view(), name='test-create'),
    # API
    path('getitems/', get_items, name='item-list-api'),
    path('getitem/<str:name>/', get_item, name='item-api')
    ]