from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Task
from django.contrib.auth import login
from .forms import ProjectForm, TaskForm, RegisterForm, TaskStatusUpdateForm

def superuser_required(user):
    return user.is_superuser

@login_required
def project_list(request):
    projects = Project.objects.filter(assigned_users=request.user)
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.user not in project.assigned_users.all():
        return redirect('project_list')
    tasks = Task.objects.filter(project=project, assigned_to=request.user)
    return render(request, 'projects/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def task_detail(request, project_id, task_id):
    task = get_object_or_404(Task, pk=task_id, project_id=project_id)
    
    if request.user == task.assigned_to or request.user.is_superuser:
        if request.method == 'POST':
            form = TaskStatusUpdateForm(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('task_detail', project_id=project_id, task_id=task_id)
        else:
            form = TaskStatusUpdateForm(instance=task)
    else:
        form = None

    return render(request, 'projects/task_detail.html', {'task': task, 'form': form})

@login_required
@user_passes_test(superuser_required)
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})

@login_required
@user_passes_test(superuser_required)
def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    
    if request.user not in project.assigned_users.all():
        return redirect('project_list')  # Redirect if user is not a member of the project
    
    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)  # Pass project instance to form
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm(project=project)  # Pass project instance to form
        
    return render(request, 'projects/task_form.html', {'form': form, 'project': project})

@login_required
@user_passes_test(superuser_required)
def task_update(request, project_pk, pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=pk)
    if request.user not in project.assigned_users.all():
        return redirect('project_list')
    if request.method == 'POST':
        form = TaskForm(project=project, data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = TaskForm(project=project, instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'project': project, 'task': task})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('project_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})