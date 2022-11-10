from django.contrib import admin

# Register your models here.

from .models import Project,  typeOfApp

class typeAdmin(admin.ModelAdmin):
    list_display = (
        'type',
    )


class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image',
        'url',
        'date',
        'category',
        # 'skills',
        'type',
    )

    ordering = ('title',)

admin.site.register(Project, ProjectAdmin)
# admin.site.register(comments)
admin.site.register(typeOfApp, typeAdmin)

