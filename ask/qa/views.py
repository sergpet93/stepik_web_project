from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from qa.itels import paginate
from qa.models import Question, Answer
from .forms import AskForm, AnswerForm
from django.views.decorators.http import require_GET

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
    form = AnswerForm(initial = {'question': id})
    return render (request, 'questions.html', {
        'question': qst,
        'answers': qst.answer_set.all(),
        'form': form,
    }) 

def ask(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})

def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    return HttpResponseRedirect('/')
