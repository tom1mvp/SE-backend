from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


from teacher_institution.models import Teacher

class ElectiveCycle(models.Model):
    year = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
        default=2026
    )
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    is_active = models.BooleanField(default=True)
    
    
    
    def __str__(self):
        return f'Year: {self.year} || Start date: {self.start_date} || End date: {self.end_date}'
    
class Course(models.Model):
    TIME_SLOT_CHOICES = [
        ('manana', 'Manana'),
        ('tarde', 'Tarde'),
        ('virtual', 'Virtual'),
    ]
    
    name = models.CharField(max_length=20, null=False)
    section = models.CharField(max_length=20, null=False)
    time_slot = models.CharField(max_length=20, choices=TIME_SLOT_CHOICES ,null=False)
    institution = models.ForeignKey('establishment.Institution', on_delete=models.PROTECT, related_name='course', null=False)
    
    def __str__(self):
        return f'Course name: {self.name} || Section: {self.section} || Time slot: {self.time_slot} || Institution: {self.institution.name}'
    
class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)
    start_time = models.TimeField(null=False, default="08:00", verbose_name="Hora de inicio")
    end_time = models.TimeField(null=False, default="12:00", verbose_name='Hora de finalización')
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='subject', null=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='subject', null=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'Name subject: {self.name} || Teacher name: {self.teacher.person.first_name}'
    
class ModalityAssistance(models.Model):
    MODALITY_CHOICES = [
        ('manana', 'Manana'),
        ('tarde', 'Tarde'),
        ('virtual', 'Virtual'),
    ]
    
    name = models.CharField(max_length=15, choices=MODALITY_CHOICES, default='manana')
    
    def __str__(self):
        return self.name
    
class Assistance(models.Model):
    date = models.DateField(default=timezone.now)
    observation = models.TextField(null=True, blank=True)
    modality = models.ForeignKey(
        ModalityAssistance, 
        on_delete=models.PROTECT, 
        related_name='assistances'
    )
    student = models.ForeignKey(
        'student_institution.Student', 
        on_delete=models.PROTECT, 
        related_name='assistances'
    )
    
    is_absence = models.BooleanField(default=False)
    
    def __str__(self):
        status = "Absence" if self.is_absence else "Present"
        return f'Student: {self.student.person.last_name} || Date: {self.date} || Modality: {self.modality} || Status: {status}'
class DisciplinaryAction(models.Model):
    REASON_CHOICES = [
        ('llamado de atención', 'Llamado de atención'),
        ('amonestado', 'Amonestado'),
        ('expulsado', 'Expulsado')
    ]
    date = models.DateField(default=timezone.now)
    reason = models.CharField(max_length=50, choices=REASON_CHOICES)
    quantity = models.IntegerField(default=0)
    observation = models.TextField(null=True, blank=True)
    student = models.ForeignKey(
        'student_institution.Student',
        on_delete=models.PROTECT,
        related_name='disciplinary_actions'
    )
    
    def __str__(self):
        return f'Student: {self.student.person.last_name} || Quantity: {self.quantity}'