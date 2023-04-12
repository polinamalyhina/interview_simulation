import random
from .models import Question

used_ids = []


def get_random_question():
    questions = Question.objects.exclude(id__in=used_ids)

    if not questions:
        used_ids.clear()
        questions = Question.objects.all()

    question = random.choice(questions)
    used_ids.append(question.id)

    return question
