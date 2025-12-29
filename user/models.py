from django.db import models

class User (models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('tutor', 'Tutor')
    ]
    
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=120, null=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    image = models.ImageField(upload_to='media/', null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Username: {self.username} || Role: {self.role} || Status: {self.is_active}'
    
