from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from polls.models import Choice, Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def owner(request):
       return HttpResponse("Hello, world. 475fe344 is the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    choice = get_object_or_404(Choice, pk=question_id)
    choice.votes += 1
    choice.save()
    return HttpResponse("You're voting on question %s." % question_id)
