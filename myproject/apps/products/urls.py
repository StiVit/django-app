from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="list"),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="detail"),
    path("create/", views.ProductCreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.ProductUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
]