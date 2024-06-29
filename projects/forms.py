from django import forms
from .models import Project, Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProjectForm(forms.ModelForm):
    assigned_users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple,
        required=True,
        label="Assign Users"
    )
    class Meta:
        model = Project
        fields = ['name', 'description', 'assigned_users']

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)  # Get project from kwargs
        super(TaskForm, self).__init__(*args, **kwargs)
        
        if project:
            self.fields['assigned_to'].queryset = project.assigned_users.all()

    class Meta:
        model = Task
        fields = ['name', 'description', 'assigned_to', 'status', 'due_date']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']