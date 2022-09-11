from django.contrib.auth.models.User
from django.db import models
class Question(models.Model):
	title = models.CharField(max_length = 255)
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	rating = models.IntegerField(default = 0)
	author = models.CharField(max_length = 255)
	likes = models.TextField()
	class QuestionManager(models.Manader):
		def new(self):
			return self.order_by('added_at')
		def popular(self):
			return self.order_by('-rating')

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateTimeField(auto_now_add = True)
	question = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)



