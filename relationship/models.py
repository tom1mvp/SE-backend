from django.db import models


from tutor_institution.models import Tutor
from student_institution.models import Student


class Relationship(models.Model):
    kinship = models.CharField(max_length=60, null=False)
    description = models.TextField(null=True, blank=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.PROTECT, related_name='tutor_relationship', null=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='student_relationship', null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        tutor_name = f"{self.tutor.person.first_name} {self.tutor.person.last_name}"
        student_name = f"{self.student.person.first_name} {self.student.person.last_name}"
        
        return f"{self.kinship} || Tutor: {tutor_name} || Student: {student_name}"