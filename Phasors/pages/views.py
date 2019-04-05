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

		receiver = "phasorsedu@gmail.com"
		sender = "chsaiteja@student.nitw.ac.in"
		rlist = []
		rlist.append(receiver)
		# try:
		send_mail('IG Connect Contact Us Message',Content,sender,rlist,fail_silently=False,)
		return redirect('/')
		# except :
		#     print 'error sending message'
		#     response['error'] = 'Error sending Message , Sorry !!!'
	return redirect('/')


def tips(request):
	response = {}
	if request.user.is_authenticated() :
		tip = Tips.objects.all()
		response['tips'] = tip
		response["auth"] = True
	else:
		tip = Tips.objects.filter(login_required = False)
		response["tips"] = tip
		response["auth"] = False

	return render(request,"pages/tips&tricks.html",response)

def comingSoon(request):
	return render(request,'pages/comingSoon.html',{})

def quiz(request):
	response = {}
	questions = Question.objects.all()
	response["questions"] = questions	
	if request.method == "POST":
		score = 0
		answer = []
		for qes in questions:
			r = {}
			r['correct'] = False
			r['ans'] = request.POST[str(qes.pk)]
			if qes.answer == request.POST[str(qes.pk)]:
				r['correct'] = True
				score+=1
			answer.append(r)
		response["answer"] = answer
		response["zipped"] = zip(questions,answer)
	return render(request, "pages/exam.html", response)

