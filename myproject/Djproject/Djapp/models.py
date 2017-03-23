from django.db import models
from django import forms
# Create your models here.
from django.contrib.auth.models import User



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class student_info(models.Model):
	name=models.CharField(max_length=500)
	password=models.CharField(max_length=50) 
	addr=models.CharField(max_length=500) 
	country=models.CharField(max_length=50) 
	state=models.CharField(max_length=500)
	phone=models.CharField(max_length=50)

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
