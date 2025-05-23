from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Question


def index(request):
    questions = Question.objects.all()
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("survey/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, 'survey/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "survey/detail.html", {"question": question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)