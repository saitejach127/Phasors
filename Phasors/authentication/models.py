# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='profile')
	ismentor = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username
