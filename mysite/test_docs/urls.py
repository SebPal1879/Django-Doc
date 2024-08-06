from django.urls import path

from . import views

app_name = "test_docs"

urlpatterns = [
    path("a/",views.iterar,name="iterar")
]
