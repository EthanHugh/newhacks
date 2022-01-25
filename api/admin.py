from django.contrib import admin
from api import models

# Register your models here.

class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ('course', )
    list_display = ('date', 'course', 'assignment_name')

admin.site.register(models.Assignment, AssignmentAdmin)
admin.site.register(models.Old_Assignment, AssignmentAdmin)