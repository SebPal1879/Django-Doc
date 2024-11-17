from django.urls import path
from . import models
from . import views

app_name = "generica1"

urlpatterns = [
    path("gen/",views.generica,name="generica")
]
