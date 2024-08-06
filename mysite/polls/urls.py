from django.urls import path

from . import views

app_name = "polls" #"app_name se usa para que Django distinga la app de la cuál se está dando la vista. Esto sirve para cuando hay muchas apps en las que puedan redundar las vistas"
urlpatterns = [
    path("ensayo/",views.vista_ensayo,name="ensayo"),
    path("",views.index, name="index"),
    path("<int:question_id>/",views.detail,name="detail"),#Envía un entero que se convierte un argumento en la vista
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote")
]
