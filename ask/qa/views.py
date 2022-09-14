from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from qa.itels import paginate
from qa.models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def main(request, *args, **kwargs):
    question = Question.objects.order_by('-added_at')
    page = paginate(request, question )
    return render (request, 'main.html', {
        'questions': page.object_list,
        'page': page,
    })
def popular(request):
    popul = Question.objects.popular()
    page = paginate(request, popul)
    return render(request, 'main.html', {
        'questions': page.object_list,
        'page': page,
    })

def question(request, id):
    qst = get_object_or_404(Question, id = id)
    return render (request, 'question.html', {
        'question': qst,
        'answers': qst.answer_set.all(),
    })
