from django.urls import include, path
from . import views

app_name = "sasunita"

urlpatterns = [
    path("sus/",views.sus,name="sus"),

]

