from django.urls import path

from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:question_id>/",views.detail,name="detail"),#Envía un entero que se convierte un argumento en la vista
    path("<int:question_id>/results/",views.results,name="results"),
    path("<int:question_id>/vote/",views.vote,name="vote")
]
