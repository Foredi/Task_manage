from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    job_types = [
        ('SV', 'Sinh viên'),
        ('GV', 'Giảng viên'),
        ('NV', 'Nhân viên')
    ]
    job_type = models.CharField(max_length=2, choices=job_types)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_types = [
        ('PT', 'Bán thời gian'),
        ('FT', 'Toàn phần')
    ]
    task_type = models.CharField(max_length=2, choices=task_types)
    time_created = models.DateTimeField(auto_now_add=True)
    time_due = models.DateTimeField()
    time_completed = models.DateTimeField(null=True, blank=True)
