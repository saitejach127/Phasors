from django.conf.urls import url
import views

urlpatterns = [
	url(r"^$", views.home),
	url(r'^portal/$', views.portal),
	url(r'^contactus/$', views.contactus),
	url(r'^tips/$',views.tips),
	url(r'^comingSoon/$',views.comingSoon),
	url(r'^practice/$', views.quiz),
]
