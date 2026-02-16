from django.urls import path
from .views import deposit, withdraw

urlpatterns = [
    path("users/<int:pk>/deposit/", deposit, name="user-deposit"),
    path("users/<int:pk>/withdraw/", withdraw, name="user-withdraw"),
]