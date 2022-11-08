from django.contrib import admin

# Register your models here.

from .models import Project, comments

admin.site.register(Project)
admin.site.register(comments)

