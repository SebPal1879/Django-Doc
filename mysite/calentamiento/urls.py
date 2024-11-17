from . import views
from django.urls import path

app_name="calentamiento"
urlpatterns = [
    path("calentamiento",views.calentamiento,name="calentamiento")
]
