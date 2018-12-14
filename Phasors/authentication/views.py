# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import *
# Create your views here.\

def signup(request):
	response = {}
	if request.user.is_authenticated() and request.user.is_active :
		return redirect("/")

	if request.method == "POST":
		user = User.objects.filter(email = request.POST["email"])
		if user.count() > 0 :
			response["error"] = "already exist"
			return render(request, "authentication/signup.html", response)

		firstname = request.POST["firstname"]
		lastname = request.POST["lastname"]
		password1 = request.POST["password1"]
		password2 = request.POST["password2"]
		email = request.POST["email"]
		username = request.POST["username"]
		if password1 != password2 :
			response["error"] = "password not match"
			return render(request, "authentication/signup.html", response)

		user = User.objects.create_user(username = username, email = email, first_name = firstname, last_name = lastname)
		user.set_password(password1)
		user.save()
		profile = Userprofile()
		profile.user = user
		profile.save()
		user = authenticate(username=username, password=password1)
		login(request, user)

		return redirect("/")
	return render(request, "authentication/signup.html", response)

def signout(request):
	logout(request)
	return redirect("/")

def signin(request):
	if request.user.is_authenticated() and request.user.is_active :
		return redirect("/")
	if request.method == "POST":
		username = request.POST["username"]
		try:
			user = User.objects.get(username=username)
			username = user.username
		except:
			try:
				user = User.objects.get(email=username)
				username = user.username
			except:
				return render(request, "authentication/login.html", {"error" : "no account"})
		password = request.POST["password"]
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/")

	return render(request,"authentication/login.html")
