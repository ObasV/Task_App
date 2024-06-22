from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('title', 'status', 'priority', 'due_date', 'assigned_to')
  list_filter = ('status', 'priority')
  search_fields = ('title', 'description')
  ordering = ['-due_date']  # Order by recent due date first

