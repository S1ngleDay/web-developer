from django import forms
from .models import BugReport, FeatureRequest

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = '__all__'
        fieldsets = (
            ('Описание проблемы', {
                'fields': ('title', 'description', 'priority', 'status'),
            }),
            ('Детали', {
                'fields': ('reported_by', 'assigned_to', 'date_reported'),
                'classes': ('collapse',),
            }),
        )
        filter_horizontal = ('tags',)

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = '__all__'
        fieldsets = (
            ('Описание запроса', {
                'fields': ('title', 'description', 'status'),
            }),
            ('Детали', {
                'fields': ('requested_by', 'assigned_to', 'date_requested'),
                'classes': ('collapse',),
            }),
        )
        filter_vertical = ('tags',)
