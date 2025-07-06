from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from myapp.models import Task


# Create your views here.

class DashBoard(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'update_task.html'
    fields = ['title', 'content', 'due_date', 'completed']
    success_url = reverse_lazy('tasks')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks')

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create_task.html'
    fields = ['user', 'title', 'content', 'due_date']
    success_url = reverse_lazy('tasks')

class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'detail_task.html'
    fields = ['user', 'title', 'content', 'created_at', 'due_date', 'completed']
