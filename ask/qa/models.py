from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')

    objects = QuestionManager()

    def __unicode__(self):
	return self.title

    def get_url(self):
	return reverse('question',args=[self.pk])

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
