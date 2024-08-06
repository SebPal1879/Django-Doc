from django.urls import path
from . import views
app_name = "fast"

urlpatterns = [
    path("xd/",views.xd,name="xd")
]
