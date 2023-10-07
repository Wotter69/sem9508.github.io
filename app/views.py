from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import tasks_db
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def todo(request):
    if request.user.username == '':
        return redirect('login')
    
    else:
        username = request.user.username
        if username == 'admin':
            user_is_admin = True
        
        else:
            user_is_admin = False

        all_tasks = tasks_db.objects.filter(user=username).values()

        context = {'all_tasks':all_tasks, 'user_is_admin':user_is_admin}
        return render(request, 'todo.html', context)

def add_task(request):
    if request.user.username == '':
        return redirect('login')
    
    else:
        task_info = request.GET['task_info']
        if task_info != "":
            task_instance = tasks_db.objects.create(task=task_info, user=request.user.username)
            task_instance.save()
        return redirect('todo')
 
def remove_task(request):
    if request.user.username == '':
        return redirect('login')

    else:
        task_info = request.GET['task_info']
        if task_info != "":
            matching_tasks = tasks_db.objects.filter(task=task_info, user=request.user.username)
            if matching_tasks.exists():
                matching_tasks.delete()
        return redirect('todo')

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('todo')
        else:
            messages.info(request, 'incorrect password or username')
            return redirect('login')

    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if username == '':
            messages.info(request, 'Please enter a valid username')
            return redirect('signup')

        else:
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username alreay used')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save();
                    return redirect('login')
            else:
                messages.info(request, 'Passwords are not the same')
                return redirect('signup')
    
    else:
        return render(request, 'signup.html')

def signout(request):
    auth.logout(request)
    return redirect('index')
