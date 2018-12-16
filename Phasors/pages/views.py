# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import smtplib
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

def contactus(request):
	response = {}
	if request.method == 'POST' :
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

		Content = 'Name : ' + name + '\n\n'
		Content = Content + 'Email : ' + email + '\n\n'
		Content = Content + 'Message : ' + message + '\n\n'
	    
		receiver = "saime0070@gmail.com"
		sender = "saime0070@gmail.com"
		rlist = []
		rlist.append(receiver)
		try:
			send_mail('IG Connect Contact Us Message',Content,sender,rlist,fail_silently=False,)
			return redirect('/')
		except :
		    print 'error sending message'
		    response['error'] = 'Error sending Message , Sorry !!!'
	return redirect('/')


def tips(request):
	data = {}
	if request.user.is_authenticated() :
		tip = Tips.objects.all()
		data['tips'] = tip
	else:
		tip = Tips.objects.filter(login_required = False)
		data["tips"] = tip
	
	return render(request,"pages/tips&tricks.html",data)
