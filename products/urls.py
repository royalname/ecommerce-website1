from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('<int:id>/', views.product_detail, name='product_detail'),
    path('<int:id>/review/', views.add_review, name='add_review'),
]