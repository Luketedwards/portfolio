from django.contrib import admin

# Register your models here.

from .models import Project, comments, typeOfApp

class typeAdmin(admin.ModelAdmin):
    list_display = (
        'type',
    )

admin.site.register(Project)
admin.site.register(comments)
admin.site.register(typeOfApp, typeAdmin)

