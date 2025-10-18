from django.shortcuts import render,redirect,get_object_or_404
from .forms import TaskForm,SignupForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=SignupForm()
    return render(request,'registration/signup.html',{'form':form})

def log_in(request):
    if request.user.is_authenticated:
       return redirect('add_task')  # already logged in, skip login page

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('add_task')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('login')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('add_task')

@login_required
def add_task(request):
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
    else:
        form =TaskForm()
    tasks=Task.objects.filter(user=request.user)
    return render(request,'todoapp/Add_task.html',{'tasks':tasks,'form':form})


    
