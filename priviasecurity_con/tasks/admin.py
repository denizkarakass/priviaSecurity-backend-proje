from django.contrib import admin

from . models import ToDoList
from . models import ToDoStep

@admin.register(ToDoList)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'updateDate', 'deleteDate', 'completedPercent')
    list_filter = ("completedPercent",)
    search_fields = ("id",)

@admin.register(ToDoStep)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'todoList', 'isCompleted')