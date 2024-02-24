from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Tag, ProjectTag


@admin.register(Project, Tag, ProjectTag)
class ProjectAdmin(admin.ModelAdmin):
    pass