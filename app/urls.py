from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task', views.add_task, name='add_task'),
    path('remove_task', views.remove_task, name='remove_task'),
    path('todo', views.todo, name='todo'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
]