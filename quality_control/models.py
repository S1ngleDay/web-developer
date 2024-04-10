from django.db import models
from django.contrib.auth.models import User
from tasks.models import Project, Task


# Create your models here.
class BugReport(models.Model):
    # Кортеж из возможных статусов задачи
    STATUS_CHOICES = [
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Очень низкий'),
        (2, 'Низкий'),
        (3, 'Средний'),
        (4, 'Высокий'),
        (5, 'Очень высокий'),
    ]

    project = models.ForeignKey(
        Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    task = models.ForeignKey(
        Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # новое поле статуса задачи
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Review',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
    )


# Create your models here.
class FeatureRequest(models.Model):
    # Кортеж из возможных статусов задачи
    STATUS_CHOICES = [
        ('Review', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    PRIORITY_CHOICES = [
        (1, 'Очень низкий'),
        (2, 'Низкий'),
        (3, 'Средний'),
        (4, 'Высокий'),
        (5, 'Очень высокий'),
    ]

    project = models.ForeignKey(
        Project,
        related_name='feature_request',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    task = models.ForeignKey(
        Task,
        related_name='feature_request',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # новое поле статуса задачи
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=3,
    )
