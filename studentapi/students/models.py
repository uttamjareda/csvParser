from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=50)
    school = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'students'
        ordering = ['created_at']
