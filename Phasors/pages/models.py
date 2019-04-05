# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tips(models.Model):
	title = models.CharField(max_length=100)
	data = models.TextField()
	login_required = models.BooleanField(default=False)

	def __str__(self):
		return self.title

class Question(models.Model):
	question = models.TextField()
	op1 = models.TextField()
	op2 = models.TextField()
	op3 = models.TextField()
	op4 = models.TextField()
	correct_choices = (
		( "op1", "option1"),
		("op2", "option2"),
		("op3", "option3"),
		("op4", "option4"),
		)
	answer = models.CharField(max_length=10,choices=correct_choices)

	def __str__(self):
		return self.question

