from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import *

urlpatterns = [
    # views
    path('', home, name='home'),
    path('test/', test_list, name='test-list'),
    path('test/new/', TestCreateView.as_view(), name='test-create'),
    path('item/', ItemListView.as_view(), name='item-list'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('item/update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('item/delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete'),
    path('tech/', tech_list, name='tech-list'),
    path('tech/new/', user_register, name='tech-create'),
    # path('tech/update/<int:pk>/', UserUpdateView.as_view(), name='tech-update'),
    path('login', LoginView.as_view(template_name = 'main/login.html'), name = 'login'),
    path('logout', LogoutView.as_view(template_name = 'main/logout.html'), name = 'logout'),
    # API
    path('getitems/', get_items, name='item-list-api'),
    path('getitem/<str:name>/', get_item, name='item-api')
    ]