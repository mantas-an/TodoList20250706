from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from myapp.models import Task


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'content', 'due_date', 'completed']

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'})
        }