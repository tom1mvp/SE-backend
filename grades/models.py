from django.db import models


from student_institution.models import Student
from academic.models import Subject


class AssessmentCategory(models.Model):
    ASSESSMENT_CATEGORY_CHOICES = [
        ("examen", 'Examen'),
        ("tp", "Trabajo Práctico"),
        ("participacion", "Participación")
    ]
    
    name = models.CharField(max_length=20, choices=ASSESSMENT_CATEGORY_CHOICES, null=False)
    
    def __str__(self):
        return self.get_name_display()

class Grade(models.Model):
    TERM_CHOICES = [
        ('primer trimestres', 'Primer Trimestre'),
        ('segundo trimestres', 'Segundo Trimestre'),
        ('tercer trimestres', 'Tercer Trimestre'),
    ]

    number = models.IntegerField(null=False)
    date = models.DateField(null=False)
    term = models.CharField(max_length=18, choices=TERM_CHOICES, default='primero', null=False)
    
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, null=False, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='grades')
    category = models.ForeignKey(AssessmentCategory, on_delete=models.PROTECT, null=False)
    
    def __str__(self):
        return f'{self.number} - {self.subject.name} - {self.get_term_display()} ({self.student.person.last_name})'