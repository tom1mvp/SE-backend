from django.db import models


from teacher_institution.models import TeachingFile

class TeacherSalary(models.Model):
    PAYMETHOD = [
        ('cash', 'Cash'),
        ('bank transfer', 'Bank transfer'),
    ]
    
    payment_date = models.DateField(null=False)
    status = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paymethod = models.CharField(max_length=20, choices=PAYMETHOD, default='cash')
    period = models.CharField(max_length=50, blank=True, null=True)
    file = models.ForeignKey(TeachingFile, on_delete=models.PROTECT, related_name='salaries', null=False)
    
    def __str__(self):
        return f'Date: {self.payment_date} || Amount: {self.amount} || Method: {self.paymethod}'
