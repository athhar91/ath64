from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'register/', views.registration, name='registerPage'),
	url(r'viewPage/', views.viewUser, name='regDetails'),
	url(r'insert/$', views.insertUser, name='insertUser'),
	url(r'viewUsers/$', views.viewFn, name='details'),
	url(r'^login/$', views.Login, name = 'login'),
	url(r'^logout/$',views.Logout, name = 'logout'),
	url(r'^user/$',views.home_user, name = 'user'),
	url(r'^index/$',views.index, name = 'index'),

  	url(r'^$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
	

	]
