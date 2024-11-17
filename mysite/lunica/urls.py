from django.urls import path
from . import views

app_name = "lunica"

urlpatterns = [
    path("lunx/",views.vistaluna,name="lunx")
]
