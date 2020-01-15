from django.urls import path
from cachorro.views import *

urlpatterns = [
    path('cadastro/', cadastro),
]  