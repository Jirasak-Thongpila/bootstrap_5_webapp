from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Student)
class SturdentAdmin(admin.ModelAdmin):
  list_display = ['stid', 'name_prefix', 'first_name', 'last_name', 'age']
  search_fields = ['stid', 'first_name', 'last_name']

@admin.register(models.Subjects)
class Subjectadmin(admin.ModelAdmin):
   list_display = ("sjid", "subjects_name", "teacher_name")
   search_fields = ("subjects_name", "teacher_name")
