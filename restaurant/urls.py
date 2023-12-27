from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-item'),
]