from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task  
from django.http import JsonResponse
from .forms import TaskForm 


#Landing page
def landing_page(request):
    tasks = Task.objects.all().order_by('-due_date') 
    context = {'task': tasks}
    return render(request, 'client/index.html', context)


# Function to display a list of all tasks
# @login_required
def task_list(request):
    tasks = Task.objects.all().order_by('-due_date')  # Order by recent due date
    context = {'task': tasks}
    return render(request, 'task_list.html', context)

# Function to display details of a specific task
# @login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})

# Function to create a new task
# @login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list.html')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'task_form.html', context)

# @login_required
def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=pk)
    else:
        form = TaskForm(instance=task)
    context = {'form': form}
    return render(request, 'task_form.html', context)


# Function to delete a task
# @login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list.html')  # Redirect to task list after deletion
    return render(request, 'task_confirm_delete.html', {'task': task})
