from django.contrib import admin
from projects.models import Project
# Register your models here.

class Project_Views(admin.ModelAdmin):
    pass

admin.site.register(Project, Project_Views)

