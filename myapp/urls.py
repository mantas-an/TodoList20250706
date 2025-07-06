from django.contrib.auth.views import LoginView
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.DashBoard.as_view(), name='home'),
    path('tasks/', views.DashBoard.as_view(), name='tasks'),
    path('update_task/<int:pk>', views.UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>', views.DeleteTask.as_view(), name='delete_task'),
    path('create_task/', views.CreateTask.as_view(), name='create_task'),
    path('detail_task/<int:pk>', views.DetailTask.as_view(), name='detail_task'),



]