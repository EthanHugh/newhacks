from django.contrib import admin
from api import models

# Register your models here.

class AssignmentAdmin(admin.ModelAdmin):
    list_filter = ('course', )

admin.site.register(models.Assignment, AssignmentAdmin)