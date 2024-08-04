from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World. You're at the Polls index")

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     #template = loader.get_template("polls/404.html")
    #     #raise Http404(template.render({"respuesta":"respuesta"},request))
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request,"polls/detail.html",{"question":question})
    # return HttpResponse("You are looking at question %s" % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)


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
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request,"polls/index.html",context)