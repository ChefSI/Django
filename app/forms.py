from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

# Create your forms here.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 100)
	last_name = forms.CharField(max_length = 100)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
 
 #for manager related form
class ManagerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class ManagerForm(forms.ModelForm):
    class Meta:
        model= Manager
        fields=['email','mobile','status','profile_pic']

#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
        
class TeacherForm(forms.ModelForm):
    class Meta:
        model= Teacher
        fields=['email','mobile','NNI','profile_pic','diplome','subject','module','status']