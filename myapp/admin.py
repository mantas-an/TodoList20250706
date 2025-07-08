from django.contrib import admin

from myapp.models import Task



class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'completed','created_at']
    list_filter = ['user']
    fieldsets = [
        ('General Info',{'fields':('title','content')}),
        ('Dates',{'fields':('due_date','completed')}),
        #TASKS paspaudus ant admin sutyeikai galimybe redaguot iis cia
    ]
    list_editable = ['completed']






# Register your models here.
admin.site.register(Task,TaskAdmin)
