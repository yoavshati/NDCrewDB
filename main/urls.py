from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('test', TestList.as_view(), name='test-list'),
    path('test/<int:pk>/', TestDetail.as_view(), name='test-detail'),
    path('test/new/', add_test, name='test-create'),
    path('test/<int:pk>/update/', TestUpdate.as_view(), name='test-update'),
    path('test/<int:pk>/delete/', TestDelete.as_view(), name='test-delete'),
    path('getitems/', get_items, name='item-list-api'),
    path('getitem/<str:name>/', get_item, name='item-api')
    ]