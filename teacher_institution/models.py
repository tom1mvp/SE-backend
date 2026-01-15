from django.db import models

from person.models import Person

class TeachingFile(models.Model):
    number = models.CharField(max_length=5, null=False, unique=True)
    license_number = models.CharField(max_length=10, null=False, unique=True)
    date_admission = models.DateField(null=False)
    
    def __str__(self):
        return f'Number: {self.number} || License: {self.license_number}'

class Teacher(models.Model):
    person = models.OneToOneField(Person, on_delete=models.PROTECT, related_name='person', null=False)
    file = models.OneToOneField(TeachingFile, on_delete=models.PROTECT, related_name='file', null=False)
    
    def __str__(self):
        return f'First name: {self.person.first_name} || Last name: {self.person.last_name} || DNI: {self.person.number_document} || File: {self.file.number}'
    
    
class TeachingAssistance(models.Model):
    ABSENCE_REASONS = [
        ('medical', 'Medical Leave'),
        ('personal', 'Personal Matters'),
        ('training', 'Professional Development'),
        ('other', 'Other'),
    ]
    date = models.DateField(null=False)
    reason = models.CharField(max_length=50, choices=ABSENCE_REASONS, null=False)
    observation = models.TextField(null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='teacher', null=False)
    
    def __str__(self):
        return f'Name: {self.teacher.person.first_name} || data: {self.date} || Number file: {self.teacher.file.number}'