from django.urls import path

from .views import *

urlpatterns = [
    # views
    path('', home, name='home'),
    path('test', TestListView.as_view(), name='test-list'),
    path('test/new/', TestCreateView.as_view(), name='test-create'),
    path('item/', ItemListView.as_view(), name='item-list'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/update/<int:id>/', ItemUpdateView.as_view(), name='item-update'),
    path('item/delete/<int:id>/', ItemDeleteView.as_view(), name='item-delete'),
    # API
    path('getitems/', get_items, name='item-list-api'),
    path('getitem/<str:name>/', get_item, name='item-api')
    ]