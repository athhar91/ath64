from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import MySQLdb as mdb
import sqlite3
from django.conf import settings
from StringIO import StringIO
from rest_framework.parsers import JSONParser
import json
from json import dumps
from django.core import serializers

# Create your views here.
#insert into database


def home_user(request):
	context={};
	return render_to_response("home.html", context, RequestContext(request))	

def home_blog(request):
	context={};
	return render_to_response("blog.html", context, RequestContext(request))	

def registration(request):
	context={};
	return render_to_response("register1.html", context, RequestContext(request))

def viewUser(request):
	context={};
	return render_to_response("view.html", context, RequestContext(request))

def insertUser(request):
	userObj = student_info()
	print "hii"
	userObj.name = request.GET.get("name",'')
	userObj.password = request.GET.get("pwdAdd",'')
	userObj.addr = request.GET.get("inserAdd",'')
	userObj.country = request.GET.get("insertCtry",'')
	userObj.state = request.GET.get("insertState",'')
	userObj.phone = request.GET.get("insertPh",'')
    #request.GET.get('name','')
	userObj.save()
	context={}
	return render_to_response("view.html",context,RequestContext(request))




def viewFn(request):
	all_users = student_info.objects.all()

	return render(request, 'view.html', {'all_users': all_users, }) 




def Login(request):
	if request.method == 'GET':
		print "hi"
		request.session['name'] = request.GET['username'] 
		return render (request, "login.html")
	else:
		print "else"
		redirect("/register1")

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)
def index(request):
	return render (request, "login.html")
def Blog(request):
	return render (request, "blog.html",{})	
	pass



def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
