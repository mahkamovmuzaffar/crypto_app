from django.urls import path
from .views import rpc_view

urlpatterns = [
    path('rpc/', rpc_view),
]
