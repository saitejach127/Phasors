from django.conf.urls import url
import views

urlpatterns = [
	url(r'^login/', views.signin),
	url(r'^signup/', views.signup),
	url(r'^logout/', views.signout),
]