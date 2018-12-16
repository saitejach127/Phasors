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

