from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import Question


def index(request):
    """Displays the latest few questions."""
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # below returns an HttpResponse object of the given template rendered with given context
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    """Displays a question text, with no results but with a form to vote."""
    # NOTE: one way to write it
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})
    # NOTE: shortcut way
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """Displays results for a particular question."""
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    """Handles voting for a particular choice in a particular question."""
    return HttpResponse("You're voting on question %s." % question_id)
