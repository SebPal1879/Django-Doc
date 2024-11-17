from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.db.models import F
from django.urls import reverse
from django.views import generic
from django.utils import timezone


# Create your views here.
# def index(request):
#     return HttpResponse("Hello World. You're at the Polls index")
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     #output = ", ".join(q.question_text for q in latest_question_list)
#     #return HttpResponse(output) 
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,- Esto es codificación rígida, debido a que se tiene que los datos están incrustrados en el código fuente y toca modificarlo mucho para esto. Esto se puede resolver haciendo un template en HTML que reciba los datos directamente
#     }
#     return HttpResponse(template.render(context, request))

#Otra manera de escribir index, usando el shortcut de render
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request,"polls/index.html",context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions (not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except:
#     #     #template = loader.get_template("polls/404.html")
#     #     #raise Http404(template.render({"respuesta":"respuesta"},request))
#     #     raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request,"polls/detail.html",{"question":question})
    # return HttpResponse("You are looking at question %s" % question_id)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



# def results(request, question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,"polls/results.html",{"question":question})
#     # response = "You are looking at the results of question %s"
#     # return HttpResponse(response % question_id)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST:
        try:
            print("aaa")
            print(request.POST["choice"])
            selected_choice = question.choice_set.get(pk=request.POST["choice"])#request.POST es un método que funciona como un diccionario que trae los datos por nombre de llave
            print("bbb")
        except(KeyError,Choice.DoesNotExist):
            return render(
                request,
                "polls/detail.html",{
                    "question":question,
                    "error_message": "You did not select a choice."
                },
            )
        else:
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))#reverse() sirve para evitar la codificación rígida, al redirigir a una página con argumentos que toma variables
    return render(request,"polls/detail.html",{"question":question})
    # return HttpResponse("You are voting on question %s" % question_id)

def vista_ensayo(request):
    contexto = "hola"
    return render(request,"polls/ensayo.html",{"context":contexto})



