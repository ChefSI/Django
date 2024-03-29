from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Manager(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='media/manager/', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True)
    status=models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.user.last_name, self.mobile)
    
    

class Subject(models.Model):
    name = models.CharField(max_length=40)
    level = models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.name
    
    

class Teacher(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='media/teacher/', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    NNI = models.CharField(max_length=10)
    diplome = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, related_name='subject')
    module = models.CharField(max_length=20, null=True, blank=True)
    langue=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.user.last_name, self.mobile)
    
    
class Establishment(models.Model):
    manager=models.OneToOneField(Manager, on_delete=models.CASCADE)
    logo= models.ImageField(upload_to='media/logo/', null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    status=models.BooleanField(default=False)
    email = models.EmailField(max_length=255)
    subject = models.ManyToManyField(Subject, related_name='subject_demanded',)
    module = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name