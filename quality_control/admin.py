from django.contrib import admin
from .models import BugReport, FeatureRequest



# класс администратора для модели BugReport
@admin.register(BugReport)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status',
                    'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'task')
    readonly_fields = ('created_at', 'updated_at')

# класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status',
                    'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'task')
    search_fields = ('title', 'description')
    list_editable = ('status', 'task')
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.

# Register your models here.
