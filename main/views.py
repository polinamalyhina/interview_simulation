from django.shortcuts import render
from .utils import get_random_question


def main(request):
    return render(request, 'main/main_page.html')


def get_question(request):
    question = get_random_question()
    context = {'question': question}
    return render(request, 'main/get_question.html', context)
