from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title','descrription','task_status','deadline']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title'
            }),
            'descrription': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task description',
                'rows': 3
            }),
            'task_status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'deadline': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make deadline field optional in form
        self.fields['deadline'].required = False

class SignupForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta():
        model =User
        fields=['username','email','password1','password2']
        widget={
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter username'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),'password1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password1'
            }),'password2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter password2'})
        }

