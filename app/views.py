from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, BadHeaderError
from .forms import UserRegisterForm, ContactForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, '', ['']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("/")
	form = ContactForm()
	return render(request, "contact.html", {'form':form})

@login_required
def subjects(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subjects.html', context)