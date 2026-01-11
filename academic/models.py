from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    
class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)
    section = models.CharField(max_length=10, null=False)
    time_slot = models.CharField(max_length=20, null=False)
    institution = models.ForeignKey('establishment.Institution', on_delete=models.PROTECT, related_name='subject', null=False)
    
    def __str__(self):
        return f'Name subject: {self.name} || Section: {self.section} || Time slot: {self.time_slot}'