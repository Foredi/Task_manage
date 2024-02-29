from django import forms
from django.contrib.auth.models import User
from .models import Profile, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'job_type']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_type', 'time_due']
