from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from .models import Question, Answer

class AskForm(forms.Form):
  title = forms.CharField(max_length=256)
  text = forms.CharField(widget=forms.Textarea)
  
  def clean_title(self):
    title = self.cleaned_data['title']
    if title.strip() == '':
      raise forms.ValidationError('Title is empty', code='validation_error')
    return title
  
  def clean_text(self):
    text = self.cleaned_data['text']
    if text.strip() == '':
      raise forms.ValidationError('Title is empty', code='validation_error')
    return text
  
  def save(self):
    #if self._user.is_anonymous():
     # self.cleaned_data['author_id'] = 1
    #else:
     # self.cleaned_data['author'] = self._user
    question = Question(**self.cleaned_data)
    question.author_id = 1
    question.save()
    return question
  
class AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
  question = forms.IntegerField(widget=forms.HiddenInput)
  
  def clean_text(self):
    text = self.cleaned_data['text']
    if text.strip() == '':
      raise forms.ValidationError('Title is empty', code='validation_error')
    return text
  
  def clean_question(self):
    try:
      question = int(self.cleaned_data['question'])
    except ValueError:
      raise forms.ValidationError('Invalid data', code='validation_error')
    return question
  
  def save(self):
    self.cleaned_data['question'] = get_object_or_404(Question, pk=self.cleaned_data['question'])
    #if self._user.is_anonymous():
     # self.cleaned_data['author_id'] = 1
    #else:
     # self.cleaned_data['author'] = self._user
    answer = Answer(**self.cleaned_data)
    answer.author_id = 1
    answer.save()
    return answer
  

