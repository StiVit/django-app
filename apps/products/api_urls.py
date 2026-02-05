from django.urls import path
from . import api_views

urlpatterns = [
    path("products/", api_views.product_list_create),
    path("products/<int:pk>/", api_views.product_detail),
]
