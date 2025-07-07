from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils import timezone
from myapp.models import Task


# Create your views here.

class DashBoard(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'




    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)   #si vieta rodo tik userio taskus

class UpdateTask(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'update_task.html'
    fields = ['title', 'content', 'due_date', 'completed']
    success_url = reverse_lazy('tasks')

    def test_func(self):
        task = self.get_object()
        return task.user == self.request.user

    #-------------------BE SITO APACIOJ---------------------
    #ISMES TIK 403 ERROR
    # def handle_no_permission(self):
    #     # Optional: Custom response if user fails test
    #     from django.http import HttpResponseForbidden
    #     return HttpResponseForbidden("🚫 Nope. This isn't your task to edit.")


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks')



class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'create_task.html'
    #fields = ['user', 'title', 'content', 'due_date']
    fields = ['title', 'content', 'due_date']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user  #automatiskai padaro loged user kaip autoriu, ir istrinam is fields user
        return super().form_valid(form)

class DetailTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'detail_task.html'
    fields = ['user', 'title', 'content', 'created_at', 'due_date', 'completed']

