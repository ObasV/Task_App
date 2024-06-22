from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['title', 'description', 'status', 'priority', 'due_date', 'category', 'assigned_to']

  def __init__(self, *args, **kwargs):
    super(TaskForm, self).__init__(*args, **kwargs)
    # Set default status to 'In Progress'
    self.fields['status'].initial = 'In Progress'
