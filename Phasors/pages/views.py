# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from authentication.models import *

# Create your views here.

def home(request):
	response = {}
	try:
		user = Userprofile.objects.get(user=request.user)
		if request.user.is_authenticated() :
			response["auth"] = True
		if user.ismentor :
			response["mentor"] = True
		else :
			response["mentor"] = False
	except:
		pass

	return render(request, "pages/index.html", response)

@login_required(login_url='/auth/signup')
def portal(request):
	user = Userprofile.objects.get(user=request.user)
	if user.ismentor :
		return render(request, "pages/mentorportal.html")
	else :
		return render(request, "pages/studentportal.html")